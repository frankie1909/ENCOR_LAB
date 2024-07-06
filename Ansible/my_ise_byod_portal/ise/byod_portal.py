# ise/byod_portal.py
from ise_api import create_byod_portal


def create_portal():
    portal_data = {
        "Portal": {
            "name": "BYOD_Portal",
            "description": "BYOD Portal for Guests",
            "portalType": "BYOD",
            # Weitere notwendige Felder hier ergänzen
        }
    }
    response = create_byod_portal(portal_data)
    return response
