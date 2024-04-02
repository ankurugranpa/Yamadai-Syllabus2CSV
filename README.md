# Yamadai-Syllabus2CSV
山形大学のシラバスのURLをCSVにまとめるスクリプトとその他関連ライブラリ群
csvファイルは学部毎に`講義番号,url`の形で出力されます。

2016年度以降のシラバスに対応





## Usage 
### シラバスのurlをcsvを作成する
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

### ライブラリとして使用
- poetryを使用する場合
`poetry add git+https://github.com/ankurugranpa/yu-syllabus.git`
- pipを使用する場合
`pip install git+https://github.com/ankurugranpa/yu-syllabus.git`

syllabsディレクトリ内にシラバスの具体的な内容を項目ごとに取得する関数があり
