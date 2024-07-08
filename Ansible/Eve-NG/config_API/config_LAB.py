from evengsdk.client import EvengClient
from pprint import pprint


client = EvengClient("localhost",
                     log_file="test.log", ssl_verify=False)
# disable warnings for self-signed certificates
client.disable_insecure_warnings()
client.login(username="silvan_adm", password="/tvOZ_D1OG.'#h37g:UV")
client.set_log_level("DEBUG")

resp = client.api.list_node_templates()
# pprint(resp.get("data"))

# Lab parameter
lab = {"name": "test_lab API", "description": "Test Lab API", "path": "/"}

# we need the lab path to create objects in the lab
lab_path = f"{lab['path']}{lab['name']}.unl"

# create management network
mgmt_cloud = {"name": "eve-mgmt", "network_type": "pnet1"}
# client.api.add_lab_network(lab_path, **mgmt_cloud)


def setup_eveng_client(host, username, password, log_file="eveng.log"):
    client = EvengClient(host, log_file=log_file, ssl_verify=False)
    client.disable_insecure_warnings()
    client.login(username=username, password=password)
    client.set_log_level("DEBUG")
    return client


def configure_node_network_settings(client, lab_path, node_name, network_settings):
    """
    Konfiguriert Netzwerkeinstellungen für einen bestimmten Node.

    :param client: EVE-NG Client-Objekt
    :param lab_path: Der Pfad des Labs
    :param node_name: Der Name des Nodes
    :param network_settings: Eine Liste von Dictionaries mit Netzwerkeinstellungen, z.B.
                             [{"interface": "Gi0/0", "ip": "192.168.1.10", "netmask": "255.255.255.0"}]
    """
    # Hier wird angenommen, dass es eine Methode gibt, um Netzwerkeinstellungen zu setzen.
    # Da die direkte API-Unterstützung variieren kann, ist dies ein Platzhalter für die tatsächliche Implementierung.
    # Möglicherweise müssen Sie die Konfigurationsdateien direkt bearbeiten oder spezielle API-Aufrufe nutzen,
    # die von Ihrer EVE-NG-Version unterstützt werden.

    # Beispiel:
    for settings in network_settings:
        interface = settings["interface"]
        ip = settings["ip"]
        netmask = settings["netmask"]
        # Hier müsste die Logik implementiert werden, um die IP-Adresse auf dem Interface zu setzen.
        print(
            f"Konfiguriere {node_name} Interface {interface} mit IP {ip} und Netmask {netmask}")
        # Beispiel für eine Implementierung könnte der Aufruf einer API-Methode sein, falls verfügbar,
        # oder das direkte Einspielen einer Konfigurationsdatei auf den Node.


def main():
    host = "localhost"
    username = "silvan_adm"
    password = "/tvOZ_D1OG.'#h37g:UV"
    client = setup_eveng_client(host, username, password)

    lab_path = "/test_lab API.unl"  # Beispiel für einen Lab-Pfad

    # Beispiel für Netzwerkeinstellungen, die konfiguriert werden sollen
    network_settings_leaf01 = [
        {"interface": "Gi0/0", "ip": "10.0.0.1", "netmask": "255.255.255.0"}]
    network_settings_leaf02 = [
        {"interface": "Gi0/0", "ip": "10.0.0.2", "netmask": "255.255.255.0"}]

    # Konfiguriere Netzwerkeinstellungen für jeden Node
    configure_node_network_settings(
        client, lab_path, "leaf01", network_settings_leaf01)
    configure_node_network_settings(
        client, lab_path, "leaf02", network_settings_leaf02)

    client.logout()


if __name__ == "__main__":
    main()


client.logout()
