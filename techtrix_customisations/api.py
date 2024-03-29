import frappe


# @frappe.whitelist()
# def get_serial_nos(args):

# 	query = frappe.db.get_list('Serial No', pluck='name')

# 	return query

@frappe.whitelist()
def get_serial_nos(doctype, txt, searchfield, start, page_len, filters):
    query = frappe.db.get_list('Serial No', filters={'item_code': filters.get('item_code'), 'warehouse': filters.get('warehouse'), 'status': 'Active'}, fields=['name'])
    return query





""" API to update sales person from heading to sales team of sales invoice"""

@frappe.whitelist()
def update_sales_team_in_sales_invoices():
    count = 0
    for inv in frappe.db.get_list('Sales Invoice', pluck='name'):
        doc = frappe.get_doc("Sales Invoice", inv)
        try:
            if doc.sales_person:
                doc.append("sales_team", {
                    "sales_person": doc.sales_person,
                    "allocated_percentage": 100
                    })
                doc.save()
                count += 1
        except Exception:
            continue


    return f"Updated {count} invoice records."