// Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Company", {
	onload: function(frm) {
		frm.set_query("default_product_customized_expense_account", function() {
			return {
				filters: {
					"company": frm.doc.name,
					"is_group": 0,
					"root_type": "Expense",
					"account_type": "Cost of Goods Sold",
				}
			};
		});
	}
})