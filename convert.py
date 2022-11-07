import json
import os
import json

json_path = "nghia_state.json"
with open(json_path, 'r', encoding='utf-8') as file:
    json_data = json.loads(file.read())
json_data['audio_paths'] = []

file_dict = {}
for root, dirs, files in os.walk(r"F:\Nghia"):
    for file in files:
        if file.endswith('.wav'):
            temp = root+'\\'+file
            temp = temp.replace('\\', '/')
            file_dict[file] = temp
            # print(root)

for msv in json_data['id']:
    for file in json_data['id'][msv]:
        json_data['id'][msv][file]['path'] = file_dict[file]

with open('nghia_state_converted.json', 'w', encoding = 'utf-8') as file:
    json.dump(json_data, file, indent = 4, ensure_ascii = False)