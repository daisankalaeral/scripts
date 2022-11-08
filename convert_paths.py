import json
import os
import argparse

def main():
    parser = argparse.ArgumentParser(usage = "Kill me")
    parser.add_argument("--input", "-i",  type = str, default = "state.json", help = "input json path")
    parser.add_argument("--dir", "-d", type = str, default = "data", help = "Directory path in which data are stored")
    parser.add_argument("--output", "-o", type = str, default = "output.json", help = "output json path")
    args = parser.parse_args()

    json_path = args.input
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

    with open(args.output, 'w', encoding = 'utf-8') as file:
        json.dump(json_data, file, indent = 4, ensure_ascii = False)

if __name__ == '__main__':
    main()