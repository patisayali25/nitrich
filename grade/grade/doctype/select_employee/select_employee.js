// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Select Employee', {
	// refresh: function(frm) {

	// }

	button: function(frm){
		 
		frm.clear_table("child")
		frm.refresh_field("child")

		frm.call({
			method: 'forggfg',
			doc: frm.doc,
		});

	}

});
