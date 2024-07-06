import requests
import json
from requests.exceptions import HTTPError
import meraki


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

dashboard = meraki.DashboardAPI(merakikey)
name = 'slu_Office'
product_types = ['appliance', 'switch', 'wireless']

response = dashboard.organizations.createOrganizationNetwork(
    orgid, name, product_types,
    tags=['AT', 'SK'],
    timeZone='Europa/Vienna',
    notes='Create network over meraki API'
)

print(response)
