from evengsdk.client import EvengClient
from pprint import pprint


client = EvengClient("34.32.39.28",
                     log_file="test.log", ssl_verify=False)
# disable warnings for self-signed certificates
client.disable_insecure_warnings()
client.login(username="silvan_adm", password="/tvOZ_D1OG.'#h37g:UV")
client.set_log_level("DEBUG")

resp = client.api.list_node_templates()
# pprint(resp.get("data"))

# create a lab
lab = {"name": "test_lab API", "description": "Test Lab API", "path": "/"}
resp = client.api.create_lab(**lab)
if resp['status'] == "success":
    print("lab created successfully.")

# we need the lab path to create objects in the lab
lab_path = f"{lab['path']}{lab['name']}.unl"

# create management network
mgmt_cloud = {"name": "eve-mgmt", "network_type": "pnet1"}
client.api.add_lab_network(lab_path, **mgmt_cloud)


# create Nodes
nodes = [
    {"name": "leaf01", "template": "viosl2",
        "image": "viosl2-adventerprisek9-m.SSA.high_iron_20200929", "left": 50},
    {"name": "leaf02", "template": "viosl2",
        "image": "viosl2-adventerprisek9-m.SSA.high_iron_20200929", "left": 200},
]
for node in nodes:
    client.api.add_node(lab_path, **node)

# connect nodes to management network
mgmt_connections = [
    {"src": "leaf01", "src_label": "Gi0/0", "dst": "eve-mgmt"},
    {"src": "leaf02", "src_label": "Gi0/0", "dst": "eve-mgmt"}
]
for link in mgmt_connections:
    client.api.connect_node_to_cloud(lab_path, **link)

# create p2p links
p2p_links = [
    {"src": "leaf01", "src_label": "Gi0/1", "dst": "leaf02", "dst_label": "Gi0/2"},
    {"src": "leaf01", "src_label": "Gi0/2", "dst": "leaf02", "dst_label": "Gi0/1"},
]
for link in p2p_links:
    client.api.connect_node_to_node(lab_path, **link)


client.logout()
