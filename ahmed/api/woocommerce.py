import frappe
from woocommerce import API
from datetime import datetime

def get_woocommerce_order_data(self, method=None):
    frappe.msgprint("get_woocommerce_order_data")
    frappe.log_error(f"\n\n\nfetching woocommerce invoices now.....\n\n\n")
    try:
        api = API(
            url="https://velobiotics.co.za",
            consumer_key="ck_465f45673a17a2fe8a09fa085015e62721887d7a",
            consumer_secret="cs_537fe200afa6c034e2abc9ba6b838c99bea89277",
            wp_api=True,
            version="wc/v3",
            timeout=3600,
        )
        source = "Woocommerce"

        page = 1
        per_page = 100
        all_orders = []

        existing_customers_array = get_current_customers()
        existing_items_array = get_current_items()
        start_date = "2023-03-01T00:00:00"
        end_date = datetime.now()

        while True:
            orders = api.get(
                "orders", params={"per_page": per_page, "page": page, "expand": "items", "after": start_date, "before": end_date}
            ).json()

            if not orders or len(orders) == 0:
                frappe.log_error(f"\n\n\n\n\n\n\n no more orders available\n\n\n\n\n\n\n")
                break
            page += 1

            all_orders.extend(orders)
            frappe.msgprint(F"{orders}")
            for order in all_orders:
                if order['status'] == "completed":
                    order_date_string = datetime.strptime(
                        order["date_created"], "%Y-%m-%dT%H:%M:%S"
                    )

                    order_date = order_date_string.strftime('%d %b %Y %H:%M:%S')
                    customer_name = (
                        order["billing"]["first_name"] + " " + order["billing"]["last_name"]
                    )
                    customer_email = order["billing"]["email"]
                    invoice_items = []
                    items = order["line_items"]

                    if not customer_name:
                        customer_name = customer_email

                    if customer_name not in existing_customers_array:
                        velobiotics.create_customer(
                            customer_name,
                            customer_type="Individual",
                            customer_group="Individual",
                            territory="South Africa",
                            customer_email=customer_email,
                        )

                    for item in items:
                        item_sku_number = item["sku"]

                        if not item_sku_number:
                            continue

                        if item_sku_number not in existing_items_array:
                            velobiotics.create_item(item["name"], item_sku_number)

                        single_item_code = frappe.db.get_value("Item", item_sku_number, "item_code")

                        rate = item["price"]
                        discount = 0
                        if rate < 1:
                            discount = 100
                            rate = 0

                        invoice_items.append(
                            {
                                "item_code": single_item_code,
                                "qty": item["quantity"],
                                "rate": rate,
                                "discount_percentage": discount,
                                "description": item['name'],
                                "income_account": "200300 - Standard Rate VAT (Value Added Tax) - 15% - V",
                            }
                        )

                        if invoice_items:
                            try:
                                isExisting = self.check_whether_invoice_exists(order['id'])
                                if not isExisting:
                                    velobiotics.create_sales_invoice(
                                        customer_name,
                                        order_date,
                                        invoice_items,
                                        source,
                                        order["id"],
                                    )
                            except Exception as e:
                                frappe.log_error("An error occurred while creating woocommerce sales invoice::: ", str(e))

        return "Woocommerce data imported successfully! No new orders available for now"
    except Exception as exception_error:
        frappe.log_error(f"\n\n\n An error occurred while pulling the woocommerce data::=> {exception_error}\n\n\n")

def get_current_customers():
    try:
        existing_customers = []
        existing_customer_object = frappe.db.get_all(
            "Customer", fields=["customer_name"]
        )

        for customer in existing_customer_object:
            if customer:
                existing_customers.append(customer.customer_name)

        return existing_customers
    except Exception as exception_error:
        frappe.log_error(str(exception_error))

def get_current_items():
    try:
        existing_items = []
        existing_item_object = frappe.db.get_all("Item", fields=["item_code"])

        for item in existing_item_object:
            existing_items.append(item.item_code)

        return existing_items
    except Exception as exception_error:
        frappe.log_error(str(exception_error))
