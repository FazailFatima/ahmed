import requests
import frappe

def dummy_api(self, method=None):
    base_url = "https://dummy.restapiexample.com"
    url = base_url + "/api/v1/employees"
    headers = {
        "Content-Type": "application/json"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        
        # Parse the JSON response data
        response_data = res.json()
        
        # Print the response data using frappe.msgprint
        frappe.msgprint(f"Response Data: {response_data}")
        
        return response_data
    
    except requests.exceptions.HTTPError as errh:
        frappe.log_error(message=str(errh), title="HTTP Error")
        return {"error": "HTTP Error occurred"}
    
    except requests.exceptions.ConnectionError as errc:
        frappe.log_error(message=str(errc), title="Connection Error")
        return {"error": "Connection Error occurred"}
    
    except requests.exceptions.Timeout as errt:
        frappe.log_error(message=str(errt), title="Timeout Error")
        return {"error": "Timeout Error occurred"}
    
    except requests.exceptions.RequestException as err:
        frappe.log_error(message=str(err), title="Request Error")
        return {"error": "An Error occurred"}

# Example usage (assuming this function is hooked properly in your Frappe app)
# result = dummy_api(None)
# print(result)
