import frappe
from frappe import _

def get_context(context):
    context.about_us_settings = frappe.get_doc('About Us Settings')
    return context

# import frappe


# def get_context(context):
#     documents = frappe.get_all("Practice", fields=["*"])
#     context["practice"] = documents