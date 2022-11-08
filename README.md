
## Một đống script vớ vẩn

### convert_paths.py
Thay đổi đường dẫn của các file audio trong `state.json` thành đường dẫn tương ứng của các file đó trong thư mục `F:\data\Nghia` trên máy. Thay đổi được lưu vào file `output.json`.
```
python convert_paths.py -i state.json -d "F:\data\Nghia" -o output.json
```

### convert_audio.py
Chuyển đổi `bit_depth`, `sample_rate`, `channels` của các file ngoại lệ về đúng chuẩn `16 bit`, `16000 Hz`, `mono`, ghi đè trực tiếp lên các file gốc. Thay đổi được lưu vào file `output.json`.
```
python convert_audio.py -i state.json -o output.json
```

### get_samples.py
Copy ngẫu nhiên một số file audio được đánh giá đạt yêu cầu ứng với từng msv vào folder `samples`.
```
python get_samples.py -i state.json -o samples
```

### remove_unqualified.py
Xóa toàn bộ các file bị đánh giá không đạt.
```
python remove_unqualified.py -i state.json
```

### stat.py
Thống kê các file đạt yêu cầu.
```
python -i state.json -o output.csv
```
|MSV       |Samples|Seconds           |Hours   |CER                |
|----------|-------|------------------|--------|-------------------|
|B18DCDT026|356    |2840.1043580000005|00:47:20|1.4330529017538856 |
|B18DCDT037|318    |2308.914636       |00:38:29|1.628884321604957  |
|B18DCDT040|266    |2091.545932000001 |00:34:52|2.7645343851826447 |
|B18DCDT048|304    |2381.676091000001 |00:39:42|0.842435355709692  |
|B18DCDT050|326    |2525.155898000001 |00:42:05|1.1552634199780898 |
|B18DCDT056|343    |1619.3434600000007|00:26:59|1.4122533748701973 |
|B18DCDT063|186    |1154.6172170000007|00:19:15|2.428411830422767  |
|B18DCDT066|256    |1574.4217609999998|00:26:14|0.7171106958146812 |
|B18DCDT069|322    |2237.120899       |00:37:17|1.32161089052751   |
|B18DCDT076|141    |1386.7384479999992|00:23:07|6.019103451761257  |
|B18DCDT077|322    |2144.131977       |00:35:44|0.7228755121756222 |
|B18DCDT080|340    |2084.1164989999993|00:34:44|1.3384020861478525 |
|B18DCDT084|305    |2230.295955999999 |00:37:10|0.18462237623199934|