// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ahmed', {
	refresh: function(frm) {
		frm.add_custom_button('Open Route form', () => {
			frappe.set_route('country',);
		})
		frm.add_custom_button('Open url form', () => {
			frappe.get_url() 
		})
		// $(document).ready(function(){
			
		// 	  $(".form-group frappe-control input-max-width col-md-2").frappe.get_route()
			  
		// 	});
		

	}
});
