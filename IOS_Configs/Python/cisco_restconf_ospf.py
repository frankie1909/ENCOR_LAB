import json
from ospf_config import configure_ospf

# Replace these with your device credentials and details
DEVICE_IP = "10.200.254.30"  # Replace with your device IP
USERNAME = "admin"  # Replace with your username
PASSWORD = "Sei8sam!"  # Replace with your password
# BASE_URL = f"https://{DEVICE_IP}:443/restconf/data"

def main():
    print("1. Fetch interfaces")
    print("2. Update hostname")
    print("3. Configure OSPF")
    choice = input("Enter your choice: ")

    if choice == "1":
        from cisco_restconf import get_interfaces  # Import only if needed
        print("Fetching interfaces...")
        interfaces = get_interfaces()
        if interfaces:
            print(json.dumps(interfaces, indent=2))
    elif choice == "2":
        from cisco_restconf import update_hostname  # Import only if needed
        new_hostname = input("Enter the new hostname: ")
        print(f"Updating hostname to {new_hostname}...")
        update_hostname(new_hostname)
    elif choice == "3":
        print("Configuring OSPF...")
        ospf_process_id = input("Enter OSPF process ID: ")
        router_id = input("Enter router ID: ")
        network = input("Enter network: ")
        wildcard_mask = input("Enter wildcard mask: ")
        area = input("Enter OSPF area: ")
        configure_ospf(DEVICE_IP, USERNAME, PASSWORD, ospf_process_id, router_id, network, wildcard_mask, area)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
