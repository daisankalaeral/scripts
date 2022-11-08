import json
import pandas as pd
import argparse
import os
import re

pattern = "\[\d[a-zA-Z][\doO][a-zA-Z][a-zA-Z0]"

def sec2hhmmss(sec, round = False):
    hours = 0
    minutes = 0

    hours = sec // 3600
    sec = sec - hours*3600
    minutes = sec//60
    seconds = sec - minutes*60
    if round:
        return '{:02.0f}:{:02.0f}:{:02.0f}'.format(hours, minutes, int(seconds))
    else:
        return '{:02.0f}:{:02.0f}:{:02.0f}'.format(hours, minutes, seconds)

def main():
    parser = argparse.ArgumentParser(usage = "Kill me")
    parser.add_argument("--input", "-i",  type = str, default = "state.json", help = "Input json path")
    parser.add_argument("--output", "-o", type = str, default = "output.csv", help = "Output csv path")
    args = parser.parse_args()

    json_path = args.input
    with open(json_path, 'r', encoding = 'utf-8') as file:
        json_data = json.loads(file.read())

    id = []
    samples = []
    duration_in_sec = []
    duration_in_hhmmss = []
    average_cer = []

    for msv, msv_val in json_data['id'].items():
        total_dist = 0
        total_len = 0
        total_samp = 0
        total_duration = 0
        for file, file_val in msv_val.items():
            if file_val['accepted'] and os.path.isfile(file_val['path']) and file_val['ref_text'].strip() and re.search(pattern, file_val['ref_text'].strip()):
                total_duration += file_val['duration']
                total_dist += file_val['distance']
                total_len += file_val['length']
                total_samp += 1
        
        id.append(msv)
        samples.append(total_samp)
        duration_in_sec.append(total_duration)
        duration_in_hhmmss.append(sec2hhmmss(total_duration))
        average_cer.append((total_dist/total_len)*100 if total_len else "?")

    df = pd.DataFrame({'MSV': id, 'Samples': samples,'Seconds': duration_in_sec, 'Hours': duration_in_hhmmss, "CER": average_cer})
    df.to_csv(args.output, index = False)
    print(f"Total samples: {sum(samples)}\nSeconds: {sum(duration_in_sec)}\nHours: {sec2hhmmss(sum(duration_in_sec))}")
    # df.to_excel(, index =False)

if __name__ == '__main__':
    main()