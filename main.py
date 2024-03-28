import re
import csv
import sys
import argparse

args = sys.argv


from lib.GetUrlList import GetUrlList as GetUrlList
from lib.FacultyDict import FacultyDict



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year",  type=int, default=2024, help="set  target year")
    parser.add_argument("-d", "--dir",  type=str, default="./", help="set directory")
    args = parser.parse_args()

    year = args.year
    directory = args.dir + "/"
    GetUrl = GetUrlList(year)
    faculty_dict = FacultyDict(year)


    for course in faculty_dict.keys():
        filename=f"{directory}{year}-{faculty_dict[course]}.csv"
        print(f"Writing...{filename}")
        kamoku_list = GetUrl.GetAtagList(course)
        with open(f"{filename}", 'w') as f:
            writer = csv.writer(f)
            for kamoku in kamoku_list:
                jyugyou_list = GetUrl.GetAtagListText(kamoku)
                for jyugyou in jyugyou_list:
                    writer.writerow(jyugyou)

if __name__ == "__main__":
    main()
