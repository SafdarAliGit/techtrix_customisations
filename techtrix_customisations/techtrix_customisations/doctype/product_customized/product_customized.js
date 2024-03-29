// Copyright (c) 2023, TNS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product Customized', {
	onload(frm){
		setup_queries(frm);
	},

	serial_nos(frm){
		if (frm.doc.type == 'Disassemble'){
			if (frm.doc.serial_nos) {
				frappe.call({
					method: "set_rate",
					doc: frm.doc,
					callback: function() {
						frm.refresh_field("basic_rate");
					}
				});

			}  else {
				// frappe.throw('')
			}
		}
	},
	
});

function setup_queries (frm) {
	frm.set_query("serial_nos", function () {
		let serial_no_filters = {}

		if (frm.doc.type == 'Assemble') {
			serial_no_filters['status']= 'Delivered'
		}

		if (frm.doc.item_code) {
			serial_no_filters["item_code"] = frm.doc.item_code;
		}

		if (frm.doc.type == 'Disassemble') {
			serial_no_filters['status']= 'Active'
			if (frm.doc.warehouse) {
				serial_no_filters["warehouse"] = frm.doc.warehouse;
			}
		}

		return {
			filters: serial_no_filters
		};
	});

	frm.set_query("item_code", function () {
		return {
			filters: {
				'is_production_item': 1,
				'has_serial_no': 1
			}
		}
	});

	frm.set_query("warehouse", function () {
		return {
			filters: {
				'is_group': 0,
				'disabled': 0,
				'company': frm.doc.company,
			}
		}
	});


	frm.fields_dict.items.grid.get_field('item_code').get_query = function() {
		return {
			filters: {
				'is_sub_assembly_item': 1,
				'has_serial_no': 1
			}
		}
	}

	frm.set_query('serial_no', 'items', function(doc, cdt, cdn) {
		var d  = locals[cdt][cdn];
		return {
			"filters": {
				"item_code": d.item_code,
				"status": 'Active'
			}
		};
	});

	frm.set_query('production_serial_no', 'items', function(doc, cdt, cdn) {
		var d  = locals[cdt][cdn];
		console.log(doc.serial_nos);
		var list_serial = doc.serial_nos.map(obj => obj.serial_no);
		return {
			"filters": {
				'name': ['in', list_serial]
			}
		};
	});
}
