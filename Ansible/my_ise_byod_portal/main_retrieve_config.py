# main_retrieve_config.py
from ise.ise_api import get_byod_portal
from wlc.wlc_api import get_guest_ssid


def main():
    print("Retrieving current BYOD Portal configuration from Cisco ISE...")
    portal_config = get_byod_portal()
    print("Current BYOD Portal configuration:", portal_config)

    print("Retrieving current GUEST SSID configuration from Cisco WLC...")
    ssid_config = get_guest_ssid()
    print("Current GUEST SSID configuration:", ssid_config)


if __name__ == "__main__":
    main()
