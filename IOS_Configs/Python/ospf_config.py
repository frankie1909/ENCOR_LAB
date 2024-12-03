import requests
import json
from requests.auth import HTTPBasicAuth

# Function to configure OSPF
def configure_ospf(device_ip, username, password, ospf_process_id, router_id, network, wildcard_mask, area):
    """
    Configure OSPF on the router using RESTCONF.
    
    :param device_ip: IP address of the device
    :param username: Username for authentication
    :param password: Password for authentication
    :param ospf_process_id: OSPF process ID
    :param router_id: Router ID for OSPF
    :param network: OSPF network
    :param wildcard_mask: Wildcard mask for the network
    :param area: OSPF area
    """
    base_url = f"https://{device_ip}:443/restconf/data"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json",
    }
    # Disable SSL warnings (only for testing purposes)
    requests.packages.urllib3.disable_warnings()

    # OSPF Configuration Payload
    payload = {
        "Cisco-IOS-XE-ospf:ospf": [
            {
                "process-id": ospf_process_id,
                "router-id": router_id,
                "network": [
                    {
                        "ip": network,
                        "wildcard": wildcard_mask,
                        "area": area
                    }
                ]
            }
        ]
    }

    # RESTCONF URL for OSPF Configuration
    url = f"{base_url}/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:ospf"

    # Send PUT Request to Configure OSPF
    response = requests.put(url, auth=HTTPBasicAuth(username, password), headers=headers, data=json.dumps(payload), verify=False)

    if response.status_code in [200, 201, 204]:
        print(f"OSPF process {ospf_process_id} configured successfully.")
    else:
        print(f"Failed to configure OSPF. Status Code: {response.status_code}")
        print(response.text)
