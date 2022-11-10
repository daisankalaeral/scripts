import json
import re

with open('vn_words.json', 'r', encoding = 'utf-8') as file:
    words = json.loads(file.read())

def check_for_irregular(text):
    temp = re.sub('\W+',' ', text.lower())
    temp = temp.split()
    result = ''
    for word in temp[1:]:
        if word not in words:
            if word.isnumeric():
                continue
            result += (word + ' ')
    if result:
        print(result)

with open('json_log/nnam_converted.json', 'r', encoding = 'utf-8') as file:
    json_data = json.loads(file.read())

for msv, msv_val in json_data['id'].items():
    for file, file_val in msv_val.items():
        if file_val['accepted']:
            text = file_val['ref_text']
            check_for_irregular(text)
