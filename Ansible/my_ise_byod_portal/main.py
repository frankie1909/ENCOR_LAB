# main.py
from ise.byod_portal import create_portal
from ise.policy_set import create_policy
from wlc.wlc_api import configure_guest_ssid
from wlc.acl import create_acl, configure_web_auth_redirect


def main():
    print("Creating BYOD Portal in Cisco ISE...")
    portal_response = create_portal()
    print("BYOD Portal created:", portal_response)

    print("Creating Policy Set in Cisco ISE...")
    policy_response = create_policy()
    print("Policy Set created:", policy_response)

    print("Configuring Guest SSID on WLC...")
    ssid_response = configure_guest_ssid()
    print("Guest SSID configured:", ssid_response)

    print("Creating ACL on WLC...")
    acl_response = create_acl()
    print("ACL created:", acl_response)

    print("Configuring Web Auth Redirect on WLC...")
    web_auth_response = configure_web_auth_redirect()
    print("Web Auth Redirect configured:", web_auth_response)


if __name__ == "__main__":
    main()
