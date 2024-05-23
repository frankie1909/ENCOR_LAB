# wlc/acl.py
import requests
from requests.auth import HTTPBasicAuth
from config import WLC_IP, WLC_USERNAME, WLC_PASSWORD

BASE_URL = f"https://{WLC_IP}/restconf/data"


def get_headers():
    return {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json"
    }


def create_acl():
    acl_data = {
        "Cisco-IOS-XE-native:ip": {
            "access-list": {
                "extended": [
                    {
                        "name": "WEB_AUTH_REDIRECT_ACL",
                        "access-list-seq-rule": [
                            {
                                "sequence": 10,
                                "permit": {
                                    "protocol": "tcp",
                                    "source-host": "any",
                                    "destination": {
                                        "destination-host": "10.0.100.100",
                                        "destination-port": {
                                            "operator": "eq",
                                            "port": "www"
                                        }
                                    }
                                }
                            },
                            {
                                "sequence": 20,
                                "permit": {
                                    "protocol": "tcp",
                                    "source-host": "any",
                                    "destination": {
                                        "destination-host": "10.0.100.100",
                                        "destination-port": {
                                            "operator": "eq",
                                            "port": "https"
                                        }
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        }
    }
    url = f"{BASE_URL}/Cisco-IOS-XE-native:native/ip/access-list"
    response = requests.put(url, headers=get_headers(), auth=HTTPBasicAuth(
        WLC_USERNAME, WLC_PASSWORD), json=acl_data, verify=False)
    return response.json()


def configure_web_auth_redirect():
    web_auth_data = {
        "Cisco-IOS-XE-wireless-client:client": {
            "web-auth": {
                "redirect": {
                    "acl": "WEB_AUTH_REDIRECT_ACL",
                    "ipv4": "10.0.100.100",
                    "port": 8443,
                    "https": True
                }
            }
        }
    }
    url = f"{BASE_URL}/Cisco-IOS-XE-wireless-client:client"
    response = requests.patch(url, headers=get_headers(), auth=HTTPBasicAuth(
        WLC_USERNAME, WLC_PASSWORD), json=web_auth_data, verify=False)
    return response.json()
