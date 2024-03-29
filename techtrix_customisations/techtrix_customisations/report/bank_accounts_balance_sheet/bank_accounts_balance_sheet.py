import frappe
from frappe import _


def execute(filters=None):
	columns, data = get_columns(), []

	# account_cond = ""
	# if filters.account:
	# 	account_cond += " and account = '%s'"%filters.account

	accounts_list = frappe.db.get_list("Account", {"is_group": 0, "account_type": "Bank"}, pluck="name")

	accounts = ", ".join("'"+acc+"'" for acc in accounts_list)	
	conditions = get_conditions(filters)
	gl_entries = frappe.db.sql("""
		select account,SUM(debit) as debit,SUM(credit) as credit, SUM(debit-credit) as balance
		from `tabGL Entry` where is_cancelled=0 and account in ({0}) {1} group by account order by account
	""".format(accounts, conditions), as_dict=True, debug=True)

	data = gl_entries
	return columns, data




def get_conditions(filters):
	cond = ""
	if filters.company:
		cond += " and company = '%s'"%filters.company
	if filters.to_date:
		cond += " and posting_date <= '%s'"%filters.to_date
	# if filters.from_date and filters.to_date:
	# 	cond += " and posting_date between '%s' and '%s'"%(filters.from_date, filters.to_date)
	if filters.account:
		cond += " and account = '%s'"%filters.account

	return cond

def get_columns():
	columns = [
		{
			"fieldname": "account",
			"fieldtype": "Link",
			"options": "Account",
			"label": _("Bank Account"),
			"width": 400,
		},
		{
			"fieldname": "debit",
			"fieldtype": "Currency",
			"label": "Amount In",
			"width": 360

		},
		{
			"fieldname": "credit",
			"fieldtype": "Currency",
			"label": "Amount Out",
			"width": 360
		},
		{
			"fieldname": "balance",
			"fieldtype": "Currency",
			"label": "Balance",
			"width": 360,
		}
	]

	return columns