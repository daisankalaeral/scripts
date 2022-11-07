import json
import os
import copy

json_path = "nghia_state_converted.json"
with open(json_path, 'r', encoding='utf-8') as file:
    json_data = json.loads(file.read())

file_list = set()

# for msv in json_data['id']:
#     for file in json_data['id'][msv]:
#         if file in file_list:
#             print(file)
#         file_list.add(file)

msv = "B18DCDT080"
new_json_data = copy.deepcopy(json_data)
for file in json_data['id'][msv]:
    if "quochoitv136" in file:
        new_name = file.replace("quochoitv136", "quochoitv136_dup")
        old_path = json_data['id'][msv][file]['path']
        new_path = os.path.dirname(json_data['id'][msv][file]['path']) + '/' + new_name
        print(new_path)
        new_json_data['id'][msv][new_name] = new_json_data['id'][msv].pop(file)
        new_json_data['id'][msv][new_name]['path'] = new_path
        print(new_json_data['id'][msv][new_name])

with open('nghia_state_converted_2.json', 'w', encoding = 'utf-8') as file:
    json.dump(new_json_data, file, indent = 4, ensure_ascii=False)