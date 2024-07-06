# https://ip-address:port/root/datastore/YANGmodule:container/leaf
import requests
import json

#router = {
#    "host": "ios-xe-mgmt.cisco.com",
#   "port": "443",
#    "user:": "developer",
#    "password": "C1sco12345"
#}

# Disable SSL Warnings for self-signed certificates
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

router = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "443",
    "user": "admin",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

#response = requests.get(url=url, headers=headers, auth=(
#    router['user'], router['password']), verify=False).json()

#print(json.dumps(response, indent=2))

response = requests.get(url=url, headers=headers, auth=(
    router['user'], router['password']), verify=False)

if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)