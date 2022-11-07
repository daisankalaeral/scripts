import json
import os

json_path = "nghia_state_converted.json"
with open(json_path, 'r', encoding='utf-8') as file:
    json_data = json.loads(file.read())

for msv in json_data['id']:
    for file in json_data['id'][msv]:
        