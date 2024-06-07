// Copyright (c) 2024, ahmed and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Work Order"] = {
		"filters": [
			{
				fieldname: 'employee_name',
				label: __('Employee Name'),
				fieldtype: 'Link',
				options: 'Employee',
			
			   
			},
			{
				fieldname: 'department',
				label: __('Department'),
				fieldtype: 'Link',
				options: 'Department',
			
			   
			},
		],
		onload: function (report) {
			report.page.add_inner_button(__("Custom Button Add to Report "),()=> {
				console.log("helooooooooooooooooooo");
			});
		},
		get_datatable_options(options) {
			return Object.assign(options, {
				cellHeight: 80
			});
		},
		// formatter: function (value, row, column, data, default_formatter) {
		// 	value = default_formatter(value, row, column, data);
		// 	if (data && data.bold) {
		// 		value = value.bold();
		// 		console.log(value)
		// 	}
		// 	return value;
		// },
		// get_datatable_options(options) {
		// 	return Object.assign(options, {
		// 		cellHeight: 150
		// 	});
		// },
};
