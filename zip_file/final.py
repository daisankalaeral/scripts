import json
import os
import re
import shutil
from tqdm import tqdm

json_dir = '/home/dell/Documents/scripts/json' #
dest_dir = '/home/dell/Documents/scripts/output'

pattern = "\[\d[a-zA-Z][\doO][a-zA-Z][a-zA-Z0]"
msv_pattern = '[a-zA-Z]\d{2}[a-zA-Z]{4}\d{3}.+'

def modify_path(path):
    new_path = re.search(msv_pattern, path)
    new_path = new_path.group() if new_path else ''
    if not new_path:
        print(f"Can't find pattern in \"{path}\"")
        return ''
    else:
        new_path = new_path.replace('\\', '/')
        return new_path

def copy_file(src_path, dest_path):
    dir_path = os.path.dirname(dest_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    shutil.copy(src_path, dest_path)

def move_stuff(file_val):
        src_path = modify_path(file_val['path'])
        if src_path:
            if file_val['accepted'] and file_val['ref_text'].strip():
                txt_path = os.path.splitext(src_path)[0] + '.txt'
                if os.path.isfile(src_path):
                    dest_path = dest_dir + '/' + src_path
                    copy_file(src_path, dest_path)
                    if os.path.isfile(txt_path):
                        dest_txt_path = dest_dir + '/' + txt_path
                        copy_file(txt_path, dest_txt_path)
                    else:
                        dest_txt_path = dest_dir + '/' + txt_path
                        with open(dest_txt_path, 'w', encoding = 'utf-8') as f:
                            f.write(file_val['ref_text'])
                else:
                    # print(f"Can't find \"{src_path}\"")
                    None
            return src_path

final_json = {}
for root, dirs, files in os.walk(json_dir):
    for file in files:
        if file.endswith('.json'):
            with open(root + '/' + file, 'r', encoding = 'utf-8') as f:
                json_data = json.loads(f.read())
            for msv, msv_val in json_data['id'].items():
                final_json.setdefault(msv, msv_val)
                if msv in final_json:
                    if len(msv_val) > len(final_json[msv]):
                        final_json[msv] = msv_val

for msv, msv_val in tqdm(final_json.items()):
    for file, file_val in msv_val.items():
        new_path = move_stuff(file_val)
        if new_path:
            final_json[msv][file]['path'] = new_path

with open('final.json', 'w', encoding = 'utf-8') as f:
    json.dump(final_json, f, indent = 4, ensure_ascii = False)