# Convert JSON to YAML and Vice-versa
import json
import yaml        # pip install pyyaml

# json.dump() method is used when the Python objects have to be stored in a file.
# json.dumps() converts a subset of Python objects into a json string.
# json.load() takes a file object and returns the json object.
# json.loads() parses a valid JSON string and convert it into a Python Dictionary.

# YML to JSON
with open('aws1.yml', 'r', encoding='utf-8') as file:
    input_file = yaml.safe_load(file)

with open('YML_TO_JSON.json', 'w', encoding='utf-8') as json_file:
    json.dump(input_file, json_file)
"""
# Print Output
with open('YML_TO_JSON.json', 'r', encoding='utf-8') as output_file:
    print(json.dumps(json.load(open('YML_TO_JSON.json')), indent=4, ensure_ascii=False))
"""

# JSON to YML
with open('aws2.json', 'r', encoding='utf-8') as file:
    input_file = json.load(file)

with open('JSON_TO_YML.yml', 'w', encoding='utf-8') as yaml_file:
    # sort_keys=False to prevent Auto sorting
    yaml.dump(input_file, yaml_file, sort_keys=False)

"""
# Print Output
with open('JSON_TO_YML.yml', 'r', encoding='utf-8') as yaml_file:
    print(yaml_file.read())
"""