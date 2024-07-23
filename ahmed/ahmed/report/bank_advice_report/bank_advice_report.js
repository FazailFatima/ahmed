// Copyright (c) 2024, Nextash SMC Pvt  and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bank Advice Report"] = {
	// onload: function (report) {
	// 	frappe.db.get_single_value('Navbar Settings', 'app_logo')
	// 	.then(app_logo => {
	// 		localStorage.setItem("logo", app_logo)
	// 	})
	// 	var defaultCompany = frappe.defaults.get_default("company");
	// 	frappe.db.get_doc('Company', defaultCompany)
    // 		.then(doc => {
	// 			frappe.db.get_value('Bank Branch', doc.custom_bank_branch, 'bank_branch_name')
	// 			.then(r => {
	// 				console.log(r.message.status) // Open
	// 				localStorage.setItem("company", JSON.stringify({ 
	// 					bank: doc.default_bank_account,
	// 					branch: r.message.bank_branch_name,
	// 					currency: doc.default_currency,
						
	// 				}))
	// 			})
    // 		})
	// },
	"filters": [
		{	
			label: "Payroll Entry",
    		fieldname: "payroll_entry",
			fieldtype: "Link",
			options : "Payroll Entry",
			on_change: function(report) {
				let payroll = frappe.query_report.get_filter_value('payroll_entry')
				if(payroll){
					frappe.db.get_doc('Payroll Entry', payroll)
					.then(payroll_doc => {
						payroll_doc.start_date
						const dateStr = payroll_doc.start_date;
						const [year, month, day] = dateStr.split('-');
						const date = new Date(year, month - 1, day);
						const monthInEnglish = date.toLocaleDateString('en-US', { month: 'long' });
						localStorage.setItem("month", JSON.stringify({ 
							month: monthInEnglish,
							year: year
						}))
						if (payroll_doc.bank_account){	
							frappe.db.get_doc('Bank Account', payroll_doc.bank_account)
							.then(bank => {
									localStorage.setItem("payroll", JSON.stringify({ 
										bank: bank.bank,
										acc_name : bank.account_name,
										acc_no : bank.bank_account_no,
									}))
							})
						} else {
							localStorage.setItem("payroll",  JSON.stringify({}))
						}
					})
				}

				report.refresh()
			}
		},
		{	
			label: "Employee Name",
    		fieldname: "employee",
			fieldtype: "Link",
			options : "Employee"
		},
		{	
			label: "Bank",
    		fieldname: "bank",
			fieldtype: "Link",
			options : "Bank"
		},
		{	
			label: "From Date",
    		fieldname: "from_date",
			fieldtype: "Date",
		},
		{	
			label: "To Date",
    		fieldname: "to_date",
			fieldtype: "Date",
		},
		{	
			label: "Status",
    		fieldname: "status",
			fieldtype: "Select",
		},
	]

};
