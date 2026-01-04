import requests
from .observability import inject_o11y_headers

def call_inventory_api(item_id: str, trace_id: str):
    # We call the contract instead of hardcoding
    headers = inject_o11y_headers(trace_id)
    
    response = requests.get(
        f"http://inventory/api/v1/{item_id}", # Just an example URL for demonstration
        headers=headers
    )
    return response.status_code