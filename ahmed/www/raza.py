# import frappe
# from frappe import _

# def get_context(context):
    # Set context variables
    # context.add_breadcrumbs = [_("Home"), "/"]
    # context.no_breadcrumbs = True
    # context.show_sidebar = False
    # context.safe_render = True
    # context.no_header = False
    # context.no_cache = True
    # context.sitemap = True
    # context.add_next_prev_links = True
    # context.title = _("Hello Page")

    # Example logic for dynamic setting of context (optional)
    # context.show_sidebar = True if some_condition else False
import frappe
from frappe import _

def get_context(context):
    # Set context variables
    context.show_sidebar = True
    context.safe_render = False
    context.no_header = False
    context.no_cache = True
    context.sitemap = False
    context.add_next_prev_links = True
    context.title = _("Hello Page")
    
    # Disable breadcrumbs by removing context settings for breadcrumbs
    context.add_breadcrumbs = [_("Home"), "/"]
    context.no_breadcrumbs = True
