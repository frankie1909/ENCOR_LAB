import requests
import json

#Disable warnings for SSL certification
requests.packages.urllib3.disable_warnings()

# Restconf API credentials and URL
HOST = '10.0.99.1'
PORT = '443'
USERNAME = 'admin'
PASSWORD = 'Cisco123!'
BASE_URL = f'https://{HOST}:{PORT}/restconf/data'

# Headers for Restconf requests

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

# Function to get interface briefs
def get_interface_brief():
    url = f'{BASE_URL}Cisco-IOS-XE-native:native/interface'
    response = requests.get(url, headers = headers, auth=(USERNAME, PASSWORD),verify=False)
    if response.ok:
        interfaces = response.json()
        print(json.dumps(interfaces, indent=2))
    else:
        print(f'Failed to retrieve interfaces: {response.text}')


# Function to create an EtherChannel
def create_etherchannel(interfae_range, channel_group_number, mode='active'):
    url = f'{BASE_URL}Cisco-IOS-XE-native:native/interface'
    payload = {
        "Cisco-IOS-XE-native:GigabitEthernet":{
            "name": interfae_range,
            "channel-group": {
                "number": channel_group_number,
                "mode": mode
            }
        }
    }
    response = requests.post(url, headers=headers, auth=(USERNAME, PASSWORD), data=json.dump(payload), verify=False)
    if response.ok:
        print(f'Etherchannel {channel_group_number} created successfully.')
    else:
        print(f'Failed to create Etherchannel: {response.text}')

# Example usage:
get_interface_brief()
# create_etherchannel('1',100,'active')