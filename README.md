# Yamadai-Syllabus2CSV
山形大学のシラバスのURLをCSVにまとめるスクリプト\
ベースURL:`https://www.yamagata-u.ac.jp/gakumu/syllabus/{年度}/`に続くように相対URLをcsvファイルに出力します。\
csvファイルは学部毎に`講義番号,url`の形をしています。\

シラバスは2016年度以降のシラバスに対応


## Usage 
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
