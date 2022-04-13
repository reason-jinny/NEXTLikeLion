def extract_info(webtoon_list):
    result = []

    for webtoon in webtoon_list:
        title = webtoon.find("td",{"class":"subject"}).find("strong").text
        artist = webtoon.find("tr").find("a",{"herf":"#"}).text
        score = webtoon.find("div",{"class":"rating_type"}).find("strong").text
        webtoon_info = {
            '제목': title,
            '작가': artist,
            '점수': score,
        }
        result.append(webtoon_info)
    return result