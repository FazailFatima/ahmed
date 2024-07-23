// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Report Print View"] = {
	"filters": [
		{
			fieldname: 'task',
			label: __('Task'),
			fieldtype: 'Data',
		
		   
		},
		{
			fieldname: 'department',
			label: __('Department'),
			fieldtype: 'Link',
			options: 'Department',
		
		   
		},
	],
	
	
};
