// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Practice', {
	refresh: function (frm) {
		frm.add_custom_button('Open Route form', () => {
			frappe.set_route('country',);
		})
		frm.add_custom_button('Open url form', () => {
			frappe.get_url("/app/doctype/Taniya")
// 
		})
// 
		// frm.add_custom_button('frm call', () => {
		// 	frm.call('send_data')

		// })
		frm.add_custom_button('Send Mail', () => {
			frm.call('send_data')

		})
		frm.add_custom_button('frappe call', () => {
			frappe.call({
				method: 'ahmed.ahmed.doctype.raza.raza.get_value',
				args: {
					'name': 'Ahmed Raza',

				},
				callback: function (r) {
					console.log(r)
				}
			});


		})
	},
});
