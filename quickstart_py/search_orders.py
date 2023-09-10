from square.client import Client
import os
from dotenv import load_dotenv
load_dotenv()
    
client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')

orders_api = client.orders

body = {
    'location_ids': [
        'LV2XZS82XY1QP'
    ],
    'query': {
        'filter': {
        }
    },
    'limit': 1,
    'return_entries': True
}

result = orders_api.search_orders(body)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
