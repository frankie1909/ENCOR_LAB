import requests
import json
from requests.exceptions import HTTPError


merakikey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = 'https://dashboard.meraki.com/api/v1'
endpoint = '/organizations'

headers = {
    'X-Cisco-Meraki-API-Key': merakikey
}

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        orgs = response.json()
        for org in orgs:
            if org['name'] == 'DevNet Sandbox':
                orgid = '549236'
except Exception as ex:
    print(ex)

endpoint = f"/organizations/{orgid}/networks"

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        nets = response.json()
except HTTPError as http:
    print(http)
except Exception as ex:
    print(ex)

netid = "L_646829496481105433"
endpoint = f"/networks/{netid}/devices"

# print(base_url + endpoint)
try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            print(device)
    else:
        print(response.status_code)
except HTTPError as http:
    print(http)
except Exception as ex:
    print(ex)
