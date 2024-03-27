# Yamadai-Syllabus2CSV
山形大学のシラバスをCSVにまとめるスクリプト
ベースURLは`https://www.yamagata-u.ac.jp/gakumu/syllabus/{年度}/`

学部毎に"講義番号, url"の形をしたcsvファイルを取得できます。
シラバスは2016年度以前には非対応


## How to Use 
poetryを使用してmain.pyを実行してください\
ex)
`poetry run python3 main.py -y 2024 -d my_dir`

```
usage: main.py [-h] [-y YEAR] [-d DIR]

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  set target year
  -d DIR, --dir DIR     set directory
```
