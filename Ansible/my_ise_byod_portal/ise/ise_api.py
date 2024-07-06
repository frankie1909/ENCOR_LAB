# ise/ise_api.py
import requests
from requests.auth import HTTPBasicAuth
from config import ISE_IP, ISE_USERNAME, ISE_PASSWORD

BASE_URL = f"https://{ISE_IP}:9060/ers/config"


def get_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


def create_byod_portal(data):
    url = f"{BASE_URL}/portal"
    response = requests.post(url, headers=get_headers(), auth=HTTPBasicAuth(
        ISE_USERNAME, ISE_PASSWORD), json=data, verify=False)
    return response.json()

# ise/ise_api.py


def get_byod_portal():
    url = f"{BASE_URL}/portal"
    response = requests.get(url, headers=get_headers(), auth=HTTPBasicAuth(
        ISE_USERNAME, ISE_PASSWORD), verify=False)
    return response.json()
