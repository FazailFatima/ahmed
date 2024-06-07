// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Practice', {
	refresh: function (frm) {
		frm.add_custom_button('Open Route form', () => {
			frappe.set_route('country',);
		})
		// frm.add_custom_button('Open url form', () => {
		// 	frappe.get_url("/app/doctype/Taniya")

		// })

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
		$(document).keydown(function (e) {
			if (e.ctrlKey && e.keyCode == 13) { // Ctrl+Enter key
				// Check if the currently focused element is within the form
				if (document.activeElement && $(document.activeElement).closest('.frappe-control').length) {
					// Add a new row to the child table
					var child = frm.add_child('practice_child');
					frm.refresh_field('practice_child');
					// Optionally, focus on the first field of the new row
					frappe.utils.scroll_to(child.wrapper);
					frm.fields_dict['practice_child'].grid.grid_rows[frm.fields_dict['practice_child'].grid.grid_rows.length - 1].toggle_view(true);
				}
			}
		});
	},
});
