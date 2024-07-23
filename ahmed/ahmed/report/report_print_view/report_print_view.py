import frappe
from datetime import datetime

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	# chart = get_chart(data)
	return columns, data,
# 
def get_columns(filters):
	columns = [
		{
			"label": "Task",
			"fieldname": "task",
			"fieldtype": "Data",
			"width": 250
		},
		{
			"label": "Amount 1",
			"fieldname": "amount_1",
			"fieldtype": "Data",
			"width": 250
		},
	
	]
	return columns

def get_data(filters):
	data = []
	emp_filters = {}
	
	if filters.get('task'):
		emp_filters['name'] = filters.get('task')
	if filters.get('department'):
		emp_filters['department'] = filters.get('department')
		
	report_data = frappe.get_list('Report Print View', emp_filters, ["*"])
	
	for report in report_data:

		data.append({
			"task": report.name,
			"amount_1": report.amount_1,
		})

	return data


# def get_chart(data):
#     return {
#         "data": {
#             "labels": ["hello", "khan", "jhan"],
#             "datasets": [{
#                 "name": "Salary",
#                 "values": [2.2, 4, 4.43, 4.432]
#             }]
#         },
#         "type": "pie",
#         "title": "This is A Practice Chart",
#         "height": 500,
#         "animate": True,
#         "truncateLegends": True# Enable animation
#     }

