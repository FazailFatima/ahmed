# Copyright (c) 2024, ahmed and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Shinza(Document):
    
    @frappe.whitelist()
    def get_data(self):
        if not hasattr(self, 'name1'):
            frappe.throw("name1 is required")
        
        # Fetch the Practice document using self.name1
        doc = frappe.get_doc("Practice", self.name1)
        
        # Clear the existing entries in table_name table if necessary
        self.set('table_name', [])
        
        # Iterate through the child table of the fetched document and add to the current document's child table
        for row in doc.practice_child:
            self.append("table_name", {
                "name1": row.name1  # Adjust the field name based on the actual structure
            })
        
        # Optionally, save the document if you want to persist changes immediately
        self.save()
        
        return self.table_name

