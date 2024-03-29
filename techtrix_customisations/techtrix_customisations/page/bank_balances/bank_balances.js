frappe.pages['bank-balances'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Bank Balances',
		single_column: true
	});
}