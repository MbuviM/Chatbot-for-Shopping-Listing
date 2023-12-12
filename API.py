import requests

url = 'https://autom.dev/api/v1/carrefour/product'
query_url = 'https://www.carrefour.ke/mafken/en/c/FKEN1600000'
api_key = 'e02c8b39-bbe3-4134-b5f3-c196939afc41'

headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

params = {
    'query': query_url
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)  # Handle the received data here
else:
    print(f"Error: {response.status_code} - {response.text}")
