def FacultyDict(year:int) -> dict:
    if year == 2016:
        faculty_list = ["人文学部", "地域教育文化学部", "理学部", "医学部", "工学部", "農学部", "基盤共通教育"]
        faculty_dict = {}
        for i in range(len(faculty_list)):
            faculty_dict[f"/{i+1}cat.htm"] = faculty_list[i]
        return faculty_dict

    else:
        faculty_list = ["人文社会科学部", "地域教育文化学部", "理学部", "医学部", "工学部", "農学部", "基盤共通教育"]
        faculty_dict = {}
        for i in range(len(faculty_list)):
            faculty_dict[f"/{i+1}cat.htm"] = faculty_list[i]
        return faculty_dict

if __name__ == "__main__":
    print(FacultyDict(2024))
