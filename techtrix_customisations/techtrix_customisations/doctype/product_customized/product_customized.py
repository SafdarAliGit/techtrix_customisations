# Copyright (c) 2023, TNS and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cint, cstr, flt
from frappe.model.document import Document
from erpnext.stock.doctype.serial_no.serial_no import (
	get_serial_nos,
	SerialNoItemError,
)
from erpnext.stock.get_item_details import get_bin_details
from frappe.model.naming import make_autoname

class ProductCustomized(Document):
	def on_submit(self):
		self.make_stock_entries()
	
	def validate(self):
		if not self.item_code:
			frappe.throw(_('Please set Production Item'))
		if not self.warehouse:
			frappe.throw(_('Please set Warehouse'))

		if self.type == 'Disassemble':
			self.check_stock()

		self.validate_serial_nos()
		self.set_rate()
		self.validate_rate()


	def validate_serial_nos(self):
		if not self.serial_nos:
			frappe.throw("Please enter Serial Nos")

		serial_nos = set(get_serial_nos(self.serial_nos))


		if self.type == 'Assemble':
			if len(serial_nos) != 1:
				frappe.throw("Only one Item can be Assembled at a time")

		if self.type == 'Disassemble':
			if cint(self.qty) != len(serial_nos):
				frappe.throw(("{0} Serial numbers required for Item {1}. You have provided {2}.").format(self.qty, self.item_code, len(serial_nos)))

		for d in self.serial_nos:
			sr = frappe.get_cached_doc('Serial No', d.serial_no)
			if sr.item_code != self.item_code:
				frappe.throw(_("Row# {0} Serial No {1} does not belong to Item {2}").format(d.idx, d.serial_no, self.item_code), SerialNoItemError)
		
		for d in self.items:
			if self.type == 'Assemble':
				if not d.serial_no:
					frappe.throw(_("Row# {0} please set Serial No").format(d.idx))

			if self.type == 'Disassemble':
				if not d.production_serial_no:
					frappe.throw(_("Row# {0} please set Production Serial No").format(d.idx))


	@frappe.whitelist()
	def set_rate(self):
		self.basic_rate = 0.0
		if self.type == 'Assemble':
			for d in self.items:
				d.basic_rate = 0.0
				for sr in list(d.serial_no.split("\n")):
					self.basic_rate += flt(frappe.get_value('Serial No', sr, 'purchase_rate'))
					d.basic_rate += self.basic_rate

		elif self.type == 'Disassemble':
			for d in self.serial_nos:
				self.basic_rate += flt(frappe.get_value('Serial No', d.serial_no, 'purchase_rate'))


	def validate_rate(self):
		if self.type == 'Disassemble':			
			parts_rate = 0.0
			for d in self.items:
				parts_rate +=  flt(d.basic_rate)
			
			if self.basic_rate != parts_rate:
				frappe.throw(_("Item rate {0} should be equal to parts rate {1}").format(self.basic_rate, parts_rate))
	
	def check_stock(self):
		bin_details = get_bin_details(self.item_code, self.warehouse)
		if bin_details.get('actual_qty') < 1:
			frappe.throw('Production Item {0} not in stock'.format(self.item_code))

	def make_stock_entries(self):
		doc = {
			"company": self.company,
			"posting_date": self.posting_date,
			"posting_time": self.posting_time,
			"name": self.name,
			"type": self.type
		}
		if self.type == 'Assemble':
			# material receipt of production item
			doc["purpose"] = "Material Receipt"
			items = []
			
			items.append({
				"item_code": self.item_code,
				"t_warehouse": self.warehouse,
				"serial_no": "\n".join([d.serial_no for d in self.serial_nos]),
				"qty": 1, # need to check
				"basic_rate": self.basic_rate,
			})
			doc['items'] = items

			make_stock_entry(doc)

			# material issue of Parts items
			doc["purpose"] = "Material Issue"
			items = []
			
			for d in self.items:
				items.append({
					"item_code": d.item_code,
					"s_warehouse": self.warehouse,
					"serial_no": d.serial_no,
					"qty": 1,
					"basic_rate": d.basic_rate,
				})
			doc['items'] = items

			make_stock_entry(doc)

		elif self.type == 'Disassemble':
			# material issue of production item
			doc["purpose"] = "Material Issue"
			items = []
			
			items.append({
				"item_code": self.item_code,
				"s_warehouse": self.warehouse,
				"serial_no": "\n".join([d.serial_no for d in self.serial_nos]),
				"qty": self.qty,
				"basic_rate": self.basic_rate,
			})
			doc['items'] = items

			make_stock_entry(doc)

			# material receipt of Parts items
				# create serial item for 
			doc["purpose"] = "Material Receipt"
			items = []
			
			for d in self.items:
				serial_no = make_autoname("{0}-{1}-.######".format(d.production_serial_no, d.item_code))
				serial_no = create_serial_no(serial_no, d.item_code)
				d.db_set("serial_no", serial_no)

				items.append({
					"item_code": d.item_code,
					"t_warehouse": self.warehouse,
					"serial_no": serial_no,
					"qty": 1,
					"basic_rate": d.basic_rate,
				})
			doc['items'] = items

			make_stock_entry(doc)	


def create_serial_no(serial_no, item_code):
	sr = frappe.new_doc("Serial No")
	sr.serial_no = serial_no
	sr.item_code = item_code
	sr.save()

	return sr.name


def make_stock_entry(doc):
	doc = frappe._dict(doc)
	receipt_entry = frappe.new_doc("Stock Entry")
	receipt_entry.company = doc.company
	receipt_entry.purpose = doc.purpose
	receipt_entry.product_customized = doc.name
	receipt_entry.product_customized_type = doc.type
	default_expense_account = frappe.get_cached_value("Company", doc.company, "default_product_customized_expense_account")
	if not default_expense_account:
		frappe.throw(_('Please set Default Product Customized Expense Account in {0}').format(frappe.get_desk_link("Company", doc.company)))


	for d in doc.get("items"):
		d['expense_account'] = default_expense_account
		receipt_entry.append("items", d)
	receipt_entry

	receipt_entry.set_stock_entry_type()
	receipt_entry.insert()
	receipt_entry.submit()