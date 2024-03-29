import frappe
from frappe import _
from .financial_statements import get_period_list

def execute(filters=None):
	

	conditions = get_conditions(filters)
	period_list = get_period_list(
		None,
		None,
		filters.from_date,
		filters.to_date,
		"Date Range",
		"Monthly",
		accumulated_values=False,
		company=None,
		reset_period_on_fy_change=True,
		ignore_fiscal_year=True,
	)

	sales_query = frappe.db.sql("""
		select SUM(sii.qty) as qty, SUM(sii.amount) amount, posting_date
		from
		`tabSales Invoice` si
		inner join `tabSales Invoice Item` sii on si.name=sii.parent
		where si.docstatus=1 {} group by si.posting_date order by si.posting_date
	""".format(conditions), as_dict=True, debug=True)

	columns, data = get_columns(period_list), []
	for record in sales_query:
		for period in period_list:
			if record.posting_date >= period.from_date and record.posting_date <= period.to_date:
				period[period.key] += record.amount
	
	row = {"description": "<h4 style='color: green;'>Sales</h4>"}
	for p in period_list:
		row[p.key] = p[p.key]

	data.append(row)

	return columns, data




def get_conditions(filters):
	cond = ""
	if filters.company:
		cond += " and company = '%s'"%filters.company
	if filters.from_date and filters.to_date:
		cond += " and si.posting_date between '%s' and '%s'"%(filters.from_date, filters.to_date)
	# if filters.account:
	# 	cond += " ,".join(acc for acc in filters.account)
	return cond

def get_columns(period_list):
	columns = [
		{
			"fieldname": "description",
			"fieldtype": "Data",
			"label": _(""),
			"default": "Sales",
			"width": 400,
		},
	]


	for period in period_list:
		columns.append({
			"fieldname": period.key,
			"fieldtype": "Currency",
			"label": _(period.label),
			"width": 180,
		})

	return columns