# Catalyst Center returns a token for username and pw auth
# x-auth-tkoen


import requests
import json

base_url = "https://dcloud-dna-center-inst-rtp.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = 'demo'
password = 'demo1234!'

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password)).json()

# returns a token

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/jscon"
}

print(token)
