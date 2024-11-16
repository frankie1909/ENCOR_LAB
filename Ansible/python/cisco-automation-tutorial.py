# Filename:                     cisco-automation-tutorial.py
# Command to run the program:   python cisco-automation-tutorial.py

# Import the required dependencies
from ncclient import manager
from jinja2 import Template

# Establish our NETCONF Session
m = manager.connect(host='10.200.254.27', port=830, username='admin',
                    password='admin', device_params={'name': 'csr'})


# Create a configuration filter with type="subtree"
interface_filter = '''
  <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
          <interface>
              <name>GigabitEthernet1</name>
          </interface>
      </interfaces>
  </filter>
'''


# Execute the get-config RPC
result = m.get_config('running', interface_filter)
print(result)


import os
print("Current Working Directory:", os.getcwd())


# Render our Jinja template
interface_template = Template(open('interface.xml').read())
interface_rendered = interface_template.render(
  INTERFACE_INDEX='4',  # Replace with the desired interface number
  IP_ADDRESS='192.168.44.1',  # Replace with the desired IP address
  SUBNET_MASK='255.255.255.0'  # Replace with the desired subnet mask
)

# Print the rendered XML for inspection (optional)
print("Rendered Configuration:")
print(interface_rendered)

# Execute the edit-config RPC with the rendered configuration
result = m.edit_config(target='running', config=interface_rendered)
print(result)

