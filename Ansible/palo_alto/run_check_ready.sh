#!/bin/bash
source venv/bin/activate
export ANSIBLE_PYTHON_INTERPRETER=$(which python)
ansible-playbook -i inventory check_ready.yml
