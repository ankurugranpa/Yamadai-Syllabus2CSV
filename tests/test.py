from yu_syllabus import GetElement

url = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/31_18053.html"
test = GetElement(url)
print(f"SubTitleSize:{test.GetSubTitleSize()}")
