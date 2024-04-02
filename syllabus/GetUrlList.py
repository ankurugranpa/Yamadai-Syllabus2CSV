import requests
from bs4 import BeautifulSoup

class GetUrlList():
    def __init__(self, year):
        self.year = year
        self.base_url = f"https://www.yamagata-u.ac.jp/gakumu/syllabus/{self.year}"


    '''
    return Atag URL List
    ex)List[AtagUrl, AtagUrl2, AtagUrl3]
    '''
    def GetAtagList(self, target_url:str) -> list:
        try:
            result = []
            abs_target_url = self.base_url + target_url 
            response = requests.get(abs_target_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                atags = soup.find_all('a')
                if atags:
                    for atag in atags:
                        href = "/" + atag.get("href") 
                        result.append(href)
                return result

            else:
                print("Failed to retrieve page:", response.status_code)
                return None
        except Exception as e:
            print("An error occurred:", str(e))
            return None

    '''
    return Atag URL List[Tapple]
    ex)List[(text, AtagUrl), (text2, AtagUrl2), (text3, AtagUrl3)]
    '''

    def GetAtagListText(self, target_url:str) -> list:
        try:
            result = []
            abs_target_url = self.base_url + target_url 
            response = requests.get(abs_target_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                atags = soup.find_all('a')
                if atags:
                    for atag in atags:
                        buf = atag.get_text(), self.base_url + "/" + atag.get("href"), 
                        result.append(buf)
                return result

            else:
                print("Failed to retrieve page:", response.status_code)
                return None
        except Exception as e:
            print("An error occurred:", str(e))
            return None


if __name__ == "__main__":
    test = GetUrlList(2024)
    print(test.GetAtagList("/home.htm"))
    print(test.GetAtagListText("/3cat.htm"))
