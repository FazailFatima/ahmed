# Copyright (c) 2024, ahmed and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from ahmed.integration.api import dummy_api

class Ahmed(Document):
	def validate(self):
		dummy_api()
