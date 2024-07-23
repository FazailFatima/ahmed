frappe.ready(function() {

	// EVENTSHANDLER

    // Bind event to the last_name field

    // frappe.web_form.on('last_name', (field, value) => {
    //     // Custom logic when the last_name field changes
    //     console.log('Last name changed:', value);
        
    //     // Show an alert with the new value
    //     frappe.msgprint(`Last name is now: ${value}`);
    // });

	//get value

	// frappe.web_form.on('last_name', (field, value) => {
    //     // Custom logic when the last_name field changes
    //     console.log('Last name changed:', value);
        
    //     // Get the value of the last_name field
    //     let lastNameValue = frappe.web_form.get_value('last_name');
        
    //     // Show an alert with the value
    //     frappe.msgprint(`Last name is now: ${lastNameValue}`);
    // });


	// Setting up the last name of Ahmed Raza
	
		// Set the value of the last_name field to "Ahmed"
		// frappe.web_form.set_value('last_name', 'Ahmed Raza');
	


	//checking before save must be the last name field exist


	// frappe.web_form.validate = () => {
	// 		// Get the value of the last_name field
	// 		let lastNameValue = frappe.web_form.get_value('last_name');
			
	// 		// Check if the last_name field is empty
	// 		if (!lastNameValue) {
	// 			// Show an alert with an error message
	// 			frappe.msgprint('Last name cannot be empty.');
				
	// 			// Return false to prevent form submission
	// 			return false;
	// 		}
			
	// 		// Return true to allow form submission
	// 		return true;};
	

	//This can use for setting property of the field
	// frappe.web_form.set_df_property('name1', 'hidden', 1);
	// frappe.web_form.set_df_property('last_name', 'reqd', 1);

	//Just working like a form control
	// frappe.web_form.after_load = () =&gt; {
		// init script here
	// }

	
	
	// Bind event to the last_name field
	// frappe.web_form.on('last_name', (field, value) => {
			// Check if the value of last_name is more than 100
			if (parseInt(value) > 100) {
				// Hide the last_name field
				frappe.web_form.set_df_property('last_name', 'hidden', 1);
			} else {
				// Show the last_name field if value is less than or equal to 100
				frappe.web_form.set_df_property('last_name', 'hidden', 0);
			}
	// });
	
	
	//Checking first the last name is less then 3 then set the value of filed is empty
	// frappe.web_form.on('last_name', (field, value) => {
        // Example condition: Check if the length of the last_name is less than 3 characters
        // if (value.length < 3) {
            // Show an alert message if the condition is met
            // frappe.msgprint('Last name must be at least 3 characters long');
            
            // Reset the last_name field value to an empty string
            // field.set_value('');
        // }





		//  // Bind an event to the last_name field
		//  frappe.web_form.on('last_name', (field, value) => {
		// 	// Check if the value of last_name is more than 100
		// 	if (parseFloat(value) > 100) {
		// 		// Hide the last_name field
		// 		frappe.web_form.set_df_property('last_name', 'hidden', 1);
		// 	} else {
		// 		// Show the last_name field if the value is less than or equal to 100
		// 		frappe.web_form.set_df_property('last_name', 'hidden', 0);
		// 	}
		// });












    });


});
