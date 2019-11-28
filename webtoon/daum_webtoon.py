import requests
import time
from .models import WebToon


def artist_name(artists):
    return artists[0].get('name') + "/" + artists[1].get('name')


def daum_webtoon_day(day):
    json_object = requests.get("http://webtoon.daum.net/data/pc/webtoon/list_serialized/" + day + "?timeStamp=" + str(time.time())).json()
    webtoon_list = json_object.get('data')
    for webtoon in webtoon_list:
        daum_webtoon = WebToon()
        daum_webtoon.webtoon_id = "다음_" + webtoon.get('title')
        daum_webtoon.webtoon_name = webtoon.get('title')
        daum_webtoon.webtoon_author = artist_name(webtoon.get('cartoon').get('artists'))
        daum_webtoon.webtoon_img_url = webtoon.get('thumbnailImage2').get('url')
        daum_webtoon.site_name = "다음"

        daum_webtoon.save()


def daum_webtoon():
    week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in week_list:
        daum_webtoon_day(day)
