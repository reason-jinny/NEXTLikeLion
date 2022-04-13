import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('webtoon.csv',mode='w',newline='')

writer = csv.writer(file)
writer.writerow(["제목","작가","점수"])

final_result = []

for page in range(1):
    WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=sat?pagingIndex=1&query=웹툰'
    webtoon_html = requests.get(WEBTOON_URL)
    webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")

    webtoon_list_box = webtoon_soup.find("ul",{"class":"img_list"})
    webtoon_list = webtoon_list_box.find_all("li")

    final_result += extract_info(webtoon_list)

for result in final_result: 
    row = []
    row.append(result['제목'])
    row.append(result['작가'])
    row.append(result['점수'])
    writer.writerow(row)

print(final_result)