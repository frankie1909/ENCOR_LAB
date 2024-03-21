from evengsdk.client import EvengClient
from pprint import pprint


client = EvengClient("localhost",
                     log_file="test.log", ssl_verify=False)
# disable warnings for self-signed certificates
client.disable_insecure_warnings()
client.login(username="silvan_adm", password="/tvOZ_D1OG.'#h37g:UV")
client.set_log_level("DEBUG")

resp = client.api.list_node_templates()
pprint(resp.get("data"))
