import requests
from bs4 import BeautifulSoup
from webtoon2 import extract_info
import csv

file = open('webtoon_listver.csv',mode='w',newline='')

writer = csv.writer(file)
writer.writerow(["제목","작가","점수"])

final_result = []

for page in range(1):
    WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=sat&view=list&order=User?pagingIndex=1&query=웹툰'
    webtoon_html = requests.get(WEBTOON_URL)
    webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")

    webtoon_list_box = webtoon_soup.find("tbody")
    webtoon_list = webtoon_list_box.find_all("tr")

    final_result += extract_info(webtoon_list)

for result in final_result: 
    row = []
    row.append(result['제목'])
    row.append(result['작가'])
    row.append(result['점수'])
    writer.writerow(row)

print(final_result)



# 아 작가 어떻게 해야할지 모르겠다 안 해!