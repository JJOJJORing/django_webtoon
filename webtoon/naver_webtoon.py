import requests
import bs4
from .models import WebToon


def naver_webtoon_day(day):
    html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=" + day)
    # print(html.status_code)
    # print(html.text)

    bs_object = bs4.BeautifulSoup(html.text, "html.parser")
    # print(bs_object
    webtoon_list = bs_object.find('div', {'class': 'list_area daily_img'})
    # print(webtoon_list)
    webtoon_list_tags = webtoon_list.findAll('li')


    for webtoon_tag in webtoon_list_tags:
        webtoon = WebToon()
        webtoon.site_name = "네이버"
        webtoon.webtoon_name = webtoon_tag.find('a')['title']
        webtoon.webtoon_author = webtoon_tag.find('dd', {'class': 'desc'}).text.strip()
        webtoon.webtoon_img_url = webtoon_tag.find('a').find('img')['src']
        webtoon.webtoon_id = "네이버_" + webtoon_tag.find('a')['title']
        # 업데이트 유무
        if webtoon_tag.find('em', {'class': 'ico_updt'}):
            webtoon.webtoon_update = 1
            # print(webtoon_tag.find('a')['title'] + ": 업데이트")
        else:
            # print(webtoon_tag.find('a')['title'] + ": 업데이트 X")
            webtoon.webtoon_update = 0
        # 휴제 유무
        if webtoon_tag.find('em', {'class': 'ico_break'}):
            # print(webtoon_tag.find('a')['title'] + ": 휴제")
            webtoon.webtoon_status = 1
        elif webtoon_tag.find('span', {'class': 'ico_new2'}):
            # print(webtoon_tag.find('a')['title'] + ": 신규")
            webtoon.webtoon_status = 2
        else:
            webtoon.webtoon_status = 0


        if day == 'mon':
            # print(webtoon_tag.find('a')['title'] + ": 월요일")
            webtoon.webtoon_mon = 1
        elif day == 'tue':
            # print(webtoon_tag.find('a')['title'] + ": 화요일")
            webtoon.webtoon_tue = 1
        elif day == 'wed':
            # print(webtoon_tag.find('a')['title'] + ": 수요일")
            webtoon.webtoon_wed = 1
        elif day == 'thu':
            # print(webtoon_tag.find('a')['title'] + ": 목요일")
            webtoon.webtoon_thu = 1
        elif day == 'fri':
            # print(webtoon_tag.find('a')['title'] + ": 금요일")
            webtoon.webtoon_fri = 1
        elif day == 'sat':
            # print(webtoon_tag.find('a')['title'] + ": 토요일")
            webtoon.webtoon_sat = 1
        else:
            # print(webtoon_tag.find('a')['title'] + ": 일요일")
            webtoon.webtoon_sun = 1

        webtoon.save()


def naver_webtoon():
    week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for week in week_list:
        naver_webtoon_day(week)

# naver_webtoon()