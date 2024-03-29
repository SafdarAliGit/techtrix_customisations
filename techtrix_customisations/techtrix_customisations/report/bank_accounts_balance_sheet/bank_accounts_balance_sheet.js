// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Bank Accounts Balance Sheet"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		// {
		// 	"fieldname":"from_date",
		// 	"label": __("From Date"),
		// 	"fieldtype": "Date",
		// 	"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		// 	"reqd": 1,
		// 	"width": "60px"
		// },
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"account",
			"label": __("Account"),
			"fieldtype": "Link",
			"options": "Account",
			get_query: function() {
				return {
					filters : {
						account_type: 'Bank',
						is_group: 0,
					}
				}
			}
		},
	]
}
