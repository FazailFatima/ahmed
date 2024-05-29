import frappe

import requests

def dummy_api():
    base_url = "https://dummy.restapiexample.com"
    url = base_url + "/api/v1/employees"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json" 
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    
    # Parse the JSON response data
    response_data = res.json()
    
    return response_data





