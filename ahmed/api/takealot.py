import frappe
import requests
import json
from datetime import datetime


def get_header():
    headers = {
        "Authorization": "Key 631db9e75face401dfd5163547b9f33889d01f1706bc8b08d613d5b544240758868bcf859e87ac35ddb3551b9b623e0d4cfbc6a46e5e139fcf738310b0e1fbdf"
    }
    return headers


def create_customer(customer_name):
    customer_doc = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": customer_name,
        'customer_type': "Individual",
        'customer_group': "Individual",
        'territory': "South Africa",
    })
    customer_doc.insert(ignore_permissions=True)
    frappe.db.commit()


def takealot_sales_data(self, method=None):
    frappe.msgprint("hello take alot")
    try:
        base_url = "http://seller-api.takealot.com/"
        url = base_url + "v2/sales"
        headers = get_header()
        all_sales_data = []
        page = 1

        today = datetime.now()
        start_date = datetime(2024, 2, 1)

        page_index = 0

        existing_invoices = frappe.get_all(
            "Sales Invoice",
            filters={
                "posting_date": ["between", [start_date, today]],
                "docstatus": ["<", 2],
                "invoice_source": "Takealot"
            },
            fields=["po_no"]
        )
        existing_order_ids = [invoice['po_no'] for invoice in existing_invoices]

        while True:
            order_ids = []
            params = {
                "page_number": page_index + 1, "filters": [
                    f"start_date:{start_date.strftime('%Y-%m-%d')}",
                    f"end_date:{today.strftime('%Y-%m-%d')}"
                ]}
            try:
                response = requests.post(url, headers=headers, params=params, timeout=3600)
                data = json.loads(response.text)
                frappe.msgprint(f"{data}")
            except Exception as e:
                frappe.log_error(f"{e}")

            if not data.get("sales"):
                frappe.log_error(f"\n\n\nno more orders available for takealot\n\n\n")
                break

            all_sales_data = list(filter(lambda sale: str(sale["order_id"]) not in existing_order_ids and sale['sale_status'] == "Shipped to Customer", data["sales"]))

            for sale in all_sales_data:
                if sale['sale_status'] == "Shipped to Customer":
                    order_ids.append(sale["order_id"])
                    order_id = sale["order_id"]

                    order_date = sale["order_date"]

                    order_date_datetime = datetime.strptime(
                        order_date, "%d %b %Y %H:%M:%S"
                    )

                    takealot_customer_name = sale["customer"]

                    existing_customer = frappe.get_all(
                        "Customer", filters={"customer_name": takealot_customer_name})

                    if not existing_customer:
                        create_customer(takealot_customer_name)

                    source = "Takealot"

                    invoice_items = []

                    item_sku = sale["sku"]

                    item_code_in_db = item_sku
                    item = sale["product_title"]

                    try:
                        invoice_items.append(
                            {
                                "item_code": item_code_in_db,
                                "item_name": item,
                                "qty": sale["quantity"],
                                "rate": float(sale["selling_price"]) / float(sale["quantity"]),
                                "income_account": "200300 - Standard Rate VAT (Value Added Tax) - 15% - V",
                                "description": item,
                            }
                        )

                        velobiotics.create_sales_invoice(
                            takealot_customer_name,
                            order_date,
                            invoice_items,
                            source,
                            order_id,
                        )
                    except Exception as issue:
                        frappe.log_error(
                            f"This error occurred while creating takealot sales invoice: {issue}")
                        frappe.log_error(type(issue).__name__)  # Log the type of exception

            frappe.log_error(f"Chunk No {page_index} Imported {len(order_ids)}", f"{order_ids}")
            page_index += 1
        return "Takealot data imported successfully!"

    except Exception as error:
        frappe.log_error(
            f"{type(error).__name__}: {error}", "An error occurred when pulling takealot invoice")


def create_customer(
        self,
        customer_name,
        customer_type="Individual",
        customer_group="Individual",
        territory="South Africa",
        customer_email=None,
):
    if customer_name:
        customer = frappe.get_doc(
            {
                "doctype": "Customer",
                "customer_name": customer_name,
                "customer_type": customer_type,
                "customer_group": customer_group,
                "email_id": customer_email,
                "territory": territory,
            }
        )
        customer.insert(ignore_permissions=True)

        frappe.db.commit()
