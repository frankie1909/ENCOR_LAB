import requests
from requests.auth import HTTPBasicAuth

def create_loopback(interface_num, ip_address, subnet_mask):
    #Device details
    url = f'https://10.10.20.48/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback={interface_num}'
    username = 'developer'
    password = 'Cisco12345'

    #Headers
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json',
    }

    #Body
    payload = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{interface_num}",
            "description": "Created by REST API",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv3": {
                "address": [
                    {
                        "ip": ip_address,
                        "netmask": subnet_mask
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    response = requests.put(url, headers = headers, payload = payload, auth=HTTPBasicAuth(username,password),verify=False)

    # Check for successful response
    if response.status_code == 200:
        print("Success!")
        print(response.text)  # or response.json() to handle JSON response
    else:
        print("Error:", response.status_code)
        print(response.text)

# Device details
url = 'https://10.10.20.48/restconf/data/Cisco-IOS-XE-native:native/interface'
username = 'developer'
password = 'C1sco12345'

# Headers - may need to adjust dependign on API
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
}

# Disable SSL Warnings for self-signed certificates
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

create_loopback(199,"10.0.0.2","255.255.255.0")

# Make the GET request with basic auth and SSL verification disabled
response = requests.get(url, headers=headers,auth=HTTPBasicAuth(username, password), verify= False)

if response.status_code == 200:
    print("Success!")
    print(response.json())
else:
    print("Error: ", response.status_code)
    print(response.text)



