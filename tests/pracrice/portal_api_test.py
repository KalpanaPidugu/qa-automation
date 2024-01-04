

import requests

base_url = "https://api.test.uksouth.vocovo.com"
url = f"{base_url}/endpoint-states?format=JSON"
location_url = f"{base_url}/locations?$limit=-37148186&$skip=-37148186"
status_url = f"{base_url}/status/v1/devices?type=all&status=online"
payload = {}

headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer 1HAHk3xT5R:c85a4c81-364d-41f7-8be5-1a05e39bc0ca'
}



if __name__ == "__main__":
    response = requests.request("GET", status_url, headers=headers, data=payload)
    print(response.text)