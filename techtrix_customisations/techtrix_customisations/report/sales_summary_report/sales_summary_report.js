// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Sales Summary Report"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
			"fieldname": "fiscal_year",
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"label": "Fiscal Year",
			// change: function(){
			// 		let fiscal_year = erpnext.utils.get_fiscal_year(frappe.datetime.get_today());

			// 	frappe.model.with_doc("Fiscal Year", fiscal_year, function(r) {
			// 		var fy = frappe.model.get_doc("Fiscal Year", fiscal_year);
			// 		console.log(fy)
			// 		frappe.query_report.set_filter_value({
			// 			from_date: fy.year_start_date,
			// 			to_date: fy.year_end_date
			// 		});
			// 	});
			// }
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"width": "60px"
		},
	],

	onload: function(){
		// let fiscal_year = erpnext.utils.get_fiscal_year(frappe.datetime.get_today());

		let date = frappe.datetime.get_today()
		let fiscal_year = '';
		frappe.call({
			method: "erpnext.accounts.utils.get_fiscal_year",
			args: {
				date: date
			},
			async: false,
			callback: function(r) {
				if (r.message) {
					fiscal_year = r.message[0];
					frappe.query_report.set_filter_value('fiscal_year', fiscal_year)
				}
			}
		});

		frappe.model.with_doc("Fiscal Year", fiscal_year, function(r) {
			var fy = frappe.model.get_doc("Fiscal Year", fiscal_year);
			frappe.query_report.set_filter_value({
				from_date: fy.year_start_date,
				to_date: fy.year_end_date
			});
		});
	}
}
