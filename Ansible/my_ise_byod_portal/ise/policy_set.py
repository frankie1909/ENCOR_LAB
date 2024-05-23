# ise/policy_set.py
from ise_api import create_policy_set


def create_policy():
    policy_data = {
        "policySet": {
            "name": "BYOD_Policy_Set",
            "description": "Policy Set for BYOD",
            "state": "enabled",
            "default": False,
            "policyCondition": {
                "conditionType": "AND",
                "isNegate": False,
                "children": [
                    {
                        "conditionType": "Simple",
                        "isNegate": False,
                        "attributeName": "NetworkAccess:NetworkDeviceName",
                        "attributeValue": "WLC9800",
                        "operator": "equals"
                    }
                ]
            },
            "authenticationPolicy": {
                "rules": [
                    {
                        "rule": {
                            "name": "BYOD_Auth_Rule",
                            "condition": {
                                "conditionType": "AND",
                                "isNegate": False,
                                "children": [
                                    {
                                        "conditionType": "Simple",
                                        "isNegate": False,
                                        "attributeName": "NetworkAccess:SSID",
                                        "attributeValue": "GUEST-SSID",
                                        "operator": "equals"
                                    }
                                ]
                            },
                            "identitySourceName": "InternalUsers"
                        }
                    }
                ]
            },
            "authorizationPolicy": {
                "rules": [
                    {
                        "rule": {
                            "name": "BYOD_Authorization_Rule",
                            "condition": {
                                "conditionType": "AND",
                                "isNegate": False,
                                "children": [
                                    {
                                        "conditionType": "Simple",
                                        "isNegate": False,
                                        "attributeName": "NetworkAccess:SSID",
                                        "attributeValue": "GUEST-SSID",
                                        "operator": "equals"
                                    }
                                ]
                            },
                            "profile": "CiscoWebAuth"
                        }
                    }
                ]
            }
        }
    }
    response = create_policy_set(policy_data)
    return response
