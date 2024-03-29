import re

import requests
from bs4 import BeautifulSoup
    

    



class GetElement():
    """Get syllubus detail
   
   Args:
    url: syllubus url
    year:  target year
    """

    def __init__(self, url, year):
        self.url = url
        self.year = year
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.element_list = soup.find_all('td')
        TAGLIST = ["授業名",
                       "ClassName",
                       "担当教員",
                       "担当教員の所属",
                       "担当教員の実務経験の有無",
                       "開講学年",
                       "開講学期",
                       "単位数",
                       "開講形態",
                       "開講対象",
                       "科目区分"]

        TAGLISTOPTONAL = ["授業名",
                       "ClassName",
                       "担当教員",
                       "担当教員の所属",
                       "担当教員の実務経験の有無",
                       "担当教員の実務経験の内容",
                       "開講学年",
                       "開講学期",
                       "単位数",
                       "開講形態",
                       "開講対象",
                       "科目区分"]
        self.tag_list = TAGLIST
        self.tag_list_op = TAGLISTOPTONAL
    

    """
    Args:
        ov_list: list of overview
    """
    def GetOverview(self) -> list:
        ov_list = []
        span_list = self.element_list[1].find_all('span')
        btag_list = self.element_list[1].find_all('b')

        if(len(btag_list) == 9):
            # print("test")
            for i in range(9+2):
                if (i < 2):
                    buf = self.tag_list[i], span_list[i].get_text()
                    ov_list.append(buf)
                else:
                    # buf = self.tag_list[i], btag_list[i-2].get_text()
                    buf = self.tag_list[i], self.element_list[1].find('b', string=f'{btag_list[i-2].get_text()}').next_sibling.strip()
                    ov_list.append(buf)


        elif(len(btag_list) == 10):
            for i in range(10+2):
                if (i < 2):
                    buf = self.tag_list[i], span_list[i].get_text()
                    ov_list.append(buf)
                else:
                    buf = self.tag_list_op[i], self.element_list[1].find('b', string=f'{btag_list[i-2].get_text()}').next_sibling.strip()
                    ov_list.append(buf)
        else:
            print("EROER")

        return ov_list



    def GetDetail(self) -> list:
        detail_list = [] # [ (title, [(sub_title,naiyou), (title, [("",naiyou)]), (title, [(sub_title,naiyou), (sub_title, naiyou)]) ]
        content_list = [] # [(sub_title,naiyou), (sub_title, naiyou)]
        btag_list = self.element_list[2].find_all('b')
        pattern = r'【.*?】'
        is_sub_title = 0 # 【が含まれているかの判定, 1の時subタイトル


        for i in range(len(btag_list)):
            if (re.match(pattern, btag_list[i].get_text()) is not None):
                 
                if btag_list[i].find_next_sibling('div') != btag_list[i+1].find_next_sibling('div') \
                        and i < len(btag_list)-1 :
                    title_html = btag_list[i]
                    title = title_html.get_text()
                    content = title_html.find_next_sibling('div').get_text().lstrip("\n")
                    tupple_buf = "", content
                    content_list.append(tupple_buf)
                    tupple_buf = title, content_list
                    detail_list.append(tupple_buf)
                    content_list = []

            else:
                sub_title_html = btag_list[i]
                sub_title = sub_title_html.get_text()
                content = sub_title_html.find_next_sibling('div').get_text().lstrip("\n")
                tupple_buf = sub_title, content
                content_list.append(tupple_buf)
                is_sub_title += 1

            if is_sub_title != 0:
                if (i == len(btag_list)-1)  or (re.match(pattern, btag_list[i+1].get_text()) is not None) :
                    tupple_buf = btag_list[i-is_sub_title].get_text(), content_list
                    detail_list.append(tupple_buf)

                    content_list = []
                    is_sub_title = 0

        return detail_list

if __name__ == "__main__":
    url = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/05_55950.html"
    url2 = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/05_52556.html"
    url3 = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/05_55001.html"
    url4 = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2016/html/05_52302.html"
    year = 2024
    class_list = []

    test = GetElement(url, year)
    test2 = GetElement(url2, year)
    test3 = GetElement(url3, year)
    test4 = GetElement(url4, 2016)
    test.GetOverview()
    test2.GetOverview()
    test3.GetOverview()
    # test3.GetDetail()
    sample_list = test4.GetDetail()
    # print(sample_list)
    for item in sample_list:
        print(item)
        print("\n")

    # print(test.GetOverview())
    print(test2.GetOverview())
    # print(test3.GetOverview())
