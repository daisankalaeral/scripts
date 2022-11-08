import json
import os
import argparse

def remove_file(src_path):
    txt_src_path = os.path.splitext(src_path)[0] + '.txt'
    
    if os.path.isfile(src_path):
        os.remove(src_path)
    if os.path.isfile(txt_src_path):
        os.remove(txt_src_path)

def main():
    parser = argparse.ArgumentParser(usage = "Kill me")
    parser.add_argument("--input", "-i",  type = str, default = "state.json", help = "Input json path")
    args = parser.parse_args()

    with open(args.input, 'r', encoding = 'utf-8') as file:
        json_data = json.loads(file.read())
    
    for msv, msv_val in json_data['id'].items():
        for file, file_val in msv_val.items():
            if not file_val['accepted']:
                remove_file(file_val['path'])

if __name__ == '__main__':
    main()