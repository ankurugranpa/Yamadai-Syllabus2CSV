import re

import requests
from bs4 import BeautifulSoup

class GetElement():
    """Get syllubus detail
   Args:
    url: syllubus url

    - This is Syllubus Struct -
    +------------+
    | ClassTitle |
    +------------+
    |  overview  |
    +------------+
    |   detail   |
    +------------+
        class_num
    """

    def __init__(self, url):
        self.url = url
        self.__cash_detail_list:list = None
        self.__cash_title_size:int = None
        self.__cash_overview_list:list = None
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.element_list = soup.find_all('td')


    def GetTitle(self) -> tuple:
        span_list = self.element_list[1].find_all('span')
        tupple_buf = span_list[0].get_text(), span_list[1].get_text()
        return tupple_buf
    

    def GetOverview(self) -> list:
        if self.__cash_overview_list is None:
            ov_list = []
            btag_list = self.element_list[1].find_all('b')

            for  item in btag_list:
                buf = item.get_text().lstrip("\u3000").rstrip("："), item.find_next_sibling(string=True).strip()
                ov_list.append(buf)
            self.__cash_overview_list = ov_list

        return self.__cash_overview_list


    def GetOvSize(self) -> int:
        return len(self.GetOverview())


    def GetDetail(self) -> list:
        if self.__cash_detail_list is None:
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
                        title = title_html.get_text().lstrip("【").rstrip("】")
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
                self.__cash_detail_list = detail_list

        return self.__cash_detail_list


    def GetClassNum(self) -> int:
        return int(self.element_list[4].get_text().split("-")[-1])


    def GetYear(self) -> int:
        return int(self.element_list[4].get_text().split("-")[-3])

    
    def GetTitleSize(self) -> int:
        if self.__cash_title_size is None:
            self.__cash_title_size = len(self.GetDetail())

        return self.__cash_title_size


    def GetSubTitleSize(self) -> int:
        size = 0
        for i in range(self.GetTitleSize()):
            for j in range(len(self.GetDetail()[i][1])):
                if self.GetDetail()[i][1][j][0] != "":
                    size += 1


        return size


if __name__ == "__main__":
    # test code
    url = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/05_55950.html"
    url2 = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/05_52556.html"
    url3 = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2024/html/05_55001.html"
    url4 = "https://www.yamagata-u.ac.jp/gakumu/syllabus/2016/html/05_52302.html"
    year = 2024
    class_list = []

    test = GetElement(url)
    test2 = GetElement(url2)
    test3 = GetElement(url3)
    test4 = GetElement(url4)

    # for item in test3.GetTitle():
    #     print(item)

    # for item in test3.GetOverview():
    #     print(item)

    # for item in test3.GetDetail():
    #     print(item)
    print(test3.GetYear())
    print(test3.GetTitleSize())
    # print(len(test3.GetDetail()[1][1]))
    print(test3.GetSubTitleSize())

