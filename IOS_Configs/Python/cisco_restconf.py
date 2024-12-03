import requests
import json
from requests.auth import HTTPBasicAuth

# Set up connection details
DEVICE_IP = "10.200.254.30"  # Replace with your device IP
USERNAME = "admin"  # Replace with your username
PASSWORD = "Sei8sam!"  # Replace with your password
BASE_URL = f"https://{DEVICE_IP}:443/restconf/data"

# Disable SSL warnings (only for testing purposes; secure deployments need valid certificates)
requests.packages.urllib3.disable_warnings()

# Headers for RESTCONF
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

def get_interfaces():
    """Retrieve all interfaces."""
    url = f"{BASE_URL}/ietf-interfaces:interfaces"
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=HEADERS, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve interfaces. Status Code: {response.status_code}")
        print(response.text)
        return None

def update_hostname(new_hostname):
    """Update the hostname."""
    url = f"{BASE_URL}/Cisco-IOS-XE-native:native/hostname"
    payload = {
        "Cisco-IOS-XE-native:hostname": new_hostname
    }
    response = requests.put(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=HEADERS, data=json.dumps(payload), verify=False)
    if response.status_code == 204:
        print(f"Hostname updated to {new_hostname}")
    else:
        print(f"Failed to update hostname. Status Code: {response.status_code}")
        print(response.text)

def main():
    # Example: Get all interfaces
    print("Fetching interfaces...")
    interfaces = get_interfaces()
    if interfaces:
        print(json.dumps(interfaces, indent=2))

    # Example: Update the hostname
    new_hostname = "Router-New"
    print(f"\nUpdating hostname to {new_hostname}...")
    update_hostname(new_hostname)

if __name__ == "__main__":
    main()
