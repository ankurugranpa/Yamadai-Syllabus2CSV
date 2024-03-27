from lib.GetUrlList import GetUrlList

GetUrlList = GetUrlList(2024)

DpUrlList = GetUrlList.GetAtagList("/home.htm")
print(DpUrlList[-1])
