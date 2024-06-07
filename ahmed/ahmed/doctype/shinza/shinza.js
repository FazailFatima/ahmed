// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shinza', {
	refresh: function(frm) {
		frm.add_custom_button('frm call', () => {
			frm.call("get_data")

		})
		frm.add_custom_button('Open Route form', () => {
			frappe.set_route('country','Afghanistan');
		})
		frm.add_custom_button('frappe call', () => {
			frappe.call({
				method: 'ahmed.ahmed.doctype.practice.practice.get_data',
				args: {
					name: 'Test'
				},
				
				callback: (r) => {
					console.log(r)
				},
			
			})
		})

	}
});
