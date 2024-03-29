import frappe
from frappe import _

def check_if_product_customisation_exist(doc, method=None):
    if doc.product_customized and frappe.db.exists('Product Customized', {"name": doc.product_customized, "docstatus": 1}):
        frappe.throw(_('Cannot cancel, because Stock entry is linked with {0}').
                     format(frappe.get_desk_link('Product Customized', doc.product_customized)))