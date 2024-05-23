import xml.etree.ElementTree as ET

# Load XML data
tree = ET.parse('/tmp/security_rules.xml')
root = tree.getroot()

# Function to parse rule details from text
def parse_rule_details(rule_text):
    details = {}
    lines = rule_text.strip().split(';')
    details['name'] = lines[0].strip('"')
    for line in lines[1:]:
        if ':' in line:
            key, value = line.split(':', 1)
            details[key.strip()] = value.strip()
    return details

# Prepare Markdown table
md_table = "| Rule Name | From Zone | To Zone | Source | Destination | Application/Service | Action |\n"
md_table += "|-----------|-----------|---------|--------|-------------|----------------------|--------|\n"

# Parse each rule
for member in root.findall('.//member'):
    rule_text = member.text
    rule = parse_rule_details(rule_text)
    md_table += f"| {rule.get('name', 'N/A')} | {rule.get('from', 'N/A')} | {rule.get('to', 'N/A')} | {rule.get('source', 'N/A')} | {rule.get('destination', 'N/A')} | {rule.get('application/service', 'N/A')} | {rule.get('action', 'N/A')} |\n"

# Write Markdown table to file
with open('/tmp/security_rules.md', 'w') as f:
    f.write(md_table)
