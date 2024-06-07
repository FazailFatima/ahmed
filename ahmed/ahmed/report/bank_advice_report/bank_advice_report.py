import frappe

def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        {	
            "label": "Employee ID",
            "fieldname": "employee",
            "fieldtype": "Data",
        },
        {	
            "label": "Employee Name",
            "fieldname": "employee_name",
            "fieldtype": "Data",
        },
        {	
            "label": "Swift Code",
            "fieldname": "swift_code",
            "fieldtype": "Data"
        },	
        {	
            "label": "Bank Code",
            "fieldname": "bank_code",
            "fieldtype": "Link",
            "options": "Employee"
        },
        {	
            "label": "Bank Sort Code",
            "fieldname": "bank_sort_code",
            "fieldtype": "Data"
        },
        {	
            "label": "Bank Name",
            "fieldname": "bank_name",
            "fieldtype": "Data"
        },
        {	
            "label": "Branch Code",
            "fieldname": "branch_code",
            "fieldtype": "Data"
        },
        {	
            "label": "Branch Name",
            "fieldname": "branch_name",
            "fieldtype": "Data"
        },
        {	
            "label": "Bank Account No",
            "fieldname": "bank_account_no",
            "fieldtype": "Data"
        },
        {	
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Data"
        },
        {	
            "label": "Description",
            "fieldname": "description",
            "fieldtype": "Data"
        },
    ]
    return columns




def get_data(filters):
    data = []
    payroll_entry = ""
    if filters.get("payroll_entry"):
        payroll_entry = filters.get("payroll_entry")
    if payroll_entry == "":
        return    
    status = 1
    my_filter = {"payroll_entry" : payroll_entry}
    if filters.get("employee"):
        my_filter['employee'] = filters.get("employee") 
    if filters.get("bank"):
        my_filter['custom_bank'] = filters.get("bank") 
    if filters.get("from_date") and filters.get("to_date"):
        my_filter['start_date'] = ("between", [filters.get("from_date"), filters.get("to_date")]) 
    if filters.get("status") == "Submitted":
        status = 1
    elif filters.get("status") == "Draft":
        status = 0
    elif filters.get("status") == "Cancelled":
        status = 2
    my_filter['docstatus'] = status 
    
    salary_slips = frappe.get_all("Salary Slip", filters=my_filter, fields=["*"], order_by = "bank_name asc")
    # group_by = filters.get("group_by")
    # frappe.msgprint(f"{salary_slips}")

    bank_name = salary_slips[0].custom_bank if len(salary_slips) > 0 else ""
    total = 0
    grand_total = 0
    total_column = "employee"
    for slip in salary_slips:
        if bank_name != slip.custom_bank:
            bank_name = slip.custom_bank
            data.append({
                total_column: "<b>Total</b>",
                "amount": f"<b>{frappe.format(total, {'fieldtype': 'Currency'})}</b>",
            })
            grand_total += total
            total = 0

        description = ""
        if slip.payroll_entry:
            payroll_doc = frappe.get_doc("Payroll Entry", slip.payroll_entry)
            description = payroll_doc.custom_description
        
        total += slip.rounded_total
        data.append({
            "employee": frappe.utils.get_link_to_form("Ahmed", slip.employee, f"{slip.employee}"),
            "employee_name": slip.name1,
            "swift_code": slip.custom_swift_code,
            "bank_code": slip.custom_bank_code,
            "bank_sort_code": slip.custom_bank_sort_code,
            "bank_name": slip.bank_name,
            "branch_code": slip.custom_bank_branch_code,
            "branch_name": slip.custom_bank_branch_name,
            "bank_account_no": slip.bank_account_no,
            "amount": frappe.format(slip.rounded_total, {'fieldtype': 'Currency'}),
            "description": description
        })
    
    data.append({
        total_column: "<b>Total</b>",
        "amount": f"<b>{frappe.format(total, {'fieldtype': 'Currency'})}</b>",
    })
    grand_total += total

    data.append({
        total_column: "<b>Grand Total</b>",
        "amount": f"<b>{frappe.format(grand_total, {'fieldtype': 'Currency'})}</b>",
    })
    
    return data
