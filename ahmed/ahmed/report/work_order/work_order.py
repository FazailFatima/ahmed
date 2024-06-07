import frappe
from datetime import datetime

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	chart = get_chart(data)
	return columns, data, None, chart

def get_columns(filters):
	columns = [
		{
			"label": "Employee",
			"fieldname": "employee",
			"fieldtype": "Data",
			"width": 250
		},
		{
			"label": "Employee Name",
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 250
		},
		{
			"label": "Image",
			"fieldname": "image",
			"fieldtype": "Image",
			"width": 250,
		},
		{
			"label": "Salary",
			"fieldname": "salary",
			"fieldtype": "Currency",
			"width": 200
		},
		{
			"label": "Department",
			"fieldname": "department",
			"fieldtype": "Data",
			"width": 250
		}
	]
	return columns

def get_data(filters):
	data = []
	emp_filters = {}
	
	if filters.get('employee_name'):
		emp_filters['name'] = filters.get('employee_name')
	if filters.get('department'):
		emp_filters['department'] = filters.get('department')
		
	employee_data = frappe.get_list('Employee', emp_filters, ["*"])
	
	for employee in employee_data:
		image_html = '<img src="{0}" style="height: auto; width: 180px !important; margin: 0 25px;">'.format(employee.image) if employee.image else ''

		data.append({
			"employee": employee.name,
			"employee_name": employee.employee_name,
			"image": image_html,
			# "salary": salary,
			"department": employee.department
		})

	return data
# def get_chart(data):
#     return {
#         "data": {
#             "labels": ["Jan", "Feb", "Mar", "Apr"],
#             "datasets": [{
#                 "name": "Revenue",
#                 "values": [10, 20, 30, 40]
#             }]
#         },
#         "type": "percentage",
#         "title": "Monthly Revenue",
#         "height": 500,
#         "animate": True,
#         "axisOptions": {
#             "xAxis": {
#                 "title": "Months",
#                 "gridLines": {
#                     "display": True,
#                     "color": "#e0e0e0"
#                 },
#                 "labels": {
#                     "display": True,
#                     "rotation": 45
#                 }
#             },
#             "yAxis": {
#                 "title": "Revenue (in thousands)",
#                 "gridLines": {
#                     "display": True,
#                     "color": "#e0e0e0"
#                 },
#                 "scale": "linear",
#                 "ticks": {
#                     "beginAtZero": True
#                 }
#             }
#         }
#     }

def get_chart(data):
    return {
        "data": {
            "labels": ["hello", "khan", "jhan"],
            "datasets": [{
                "name": "Salary",
                "values": [2.2, 4, 4.43, 4.432]
            }]
        },
        "type": "pie",
        "title": "This is A Practice Chart",
        "height": 500,
        "animate": True,
        "truncateLegends": True# Enable animation
    }


# def get_chart(data):
# 	labels = [d['employee'] for d in data]
# 	salaries = [d['employee_name'] for d in data]

# 	return {
# 		"data": {
# 			"labels": labels,
# 			"datasets": [{
# 				"name": "Salary",
# 				"values": salaries
# 			}]
# 		},
# 		"type": "line",  # You can change this to 'line', 'pie', etc.
# 		"colors": ["#7cd6fd"],
# 		"barOptions": {
# 			"stacked": True
# 		}
# 	}