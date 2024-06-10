# Copyright (c) 2024, ahmed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



class Practice(Document):

	@frappe.whitelist()
	def	send_data(self):
		email = "shinzaaslam@gmail.com"
		sender = frappe.session.user
		subject = "Subject of the email"
		message = "This is the body of the email."
		frappe.sendmail(
        recipients=email,
        sender=None,
        subject=subject,
        message=message,
        header=[subject, "green"],
        delayed= False,
        retry=3,
    )
	frappe.msgprint("send the mail successfuly")
		# val=frappe.msgprint("send the mail successfuly")
		# return val
	 


