# PAN-OS Ansible Playbook

This playbook retrieves the running configuration from a PAN-OS device using the `panos_op` module from the `paloaltonetworks.panos` collection.

## Setup

1. Ensure you have the necessary Ansible collection:
   ```bash
   ansible-galaxy collection install paloaltonetworks.panos

ansible-playbook plays/read_config.yml


ansible-galaxy collection install paloaltonetworks.panos


# Installiere Ansible, falls noch nicht geschehen
pip install ansible

# Installiere die PAN-OS Ansible Collection
ansible-galaxy collection install paloaltonetworks.panos

# Überprüfe die Installation
ansible-galaxy collection list

# Führe das Playbook aus
ansible-playbook plays/read_config.yml


# PAN-OS Ansible Playbook

This playbook retrieves the running configuration from a PAN-OS device, splits it into modular configuration files, and applies these configurations.

## Setup

1. Ensure you have the necessary Ansible collection:
   ```bash
   ansible-galaxy collection install paloaltonetworks.panos

ansible-playbook plays/read_config.yml
ansible-playbook plays/split_config.yml
