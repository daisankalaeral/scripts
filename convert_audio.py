import json
import os
import subprocess
import argparse

def convert(file_path):
    if not os.path.isfile(file_path):
        print(f"Can't find {file_path}")
        return
    ecec = os.path.splitext(file_path)
    temp_path = ecec[0]+'_temp'+ecec[1]
    command = fr'ffmpeg -i "{file_path}" -y -ar 16000 -ac 1 -sample_fmt s16 "{temp_path}"'
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True, shell = True)
    process.wait()
    stdout, stderr = process.communicate()
    if stdout:
        print(file_path)
        print(stdout)
    else:
        os.replace(temp_path, file_path)
def main():
    parser = argparse.ArgumentParser(usage = "Kill me")
    parser.add_argument("--input", "-i",  type = str, default = "state.json", help = "Input json path")
    parser.add_argument("--output", "-o", type = str, default = "output.json", help = "Output json path")
    args = parser.parse_args()

    json_path = args.input
    with open(json_path, 'r', encoding='utf-8') as file:
        json_data = json.loads(file.read())

    for msv in json_data['id']:
        for file in json_data['id'][msv]:
            if json_data['id'][msv][file]['accepted']:
                file_path = json_data['id'][msv][file]['path']
                n_bits, sample_rate, channels = json_data['id'][msv][file]['n_bits'], json_data['id'][msv][file]['sample_rate'], json_data['id'][msv][file]['channels'] 
                if n_bits != 16 or sample_rate != 16000 or channels != 1:
                    # print(file_path, sample_rate, channels)
                    convert(file_path)
                    json_data['id'][msv][file]['n_bits'] = 16
                    json_data['id'][msv][file]['sample_rate'] = 16000
                    json_data['id'][msv][file]['channels'] = 1

    with open(args.output, 'w', encoding = 'utf-8') as file:
        json.dump(json_data, file, indent = 4, ensure_ascii = False)

if __name__ == '__main__':
    main()