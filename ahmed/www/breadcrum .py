import frappe
from frappe import _

def get_context(context):
    # frappe.utils.add_breadcrumbs(_("Home"), "/")
    # frappe.breadcrumbs.clear()
    context.no_breadcrumbs = True



    # Add other context variables if needed
    context.title = _("Hello Page")
