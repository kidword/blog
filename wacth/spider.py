# encoding=utf-8
from watch.cookie import GetCookie
import requests
import random
from queue import Queue
from fake_useragent import UserAgent
from lxml import etree


class WatchIndex:
    def __init__(self):
        # self.url_q = Queue()
        self.start_url = 'https://www.aliexpress.com/wholesale?site=glo&g=y&SearchText=women+watches&page={}'

    def request(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        get_cookies = GetCookie()
        cookie_lis = get_cookies.get_cookie()  # 获取cookie
        cookies = random.choice(cookie_lis)
        if cookies:
            s = requests.Session()
            for cookie in cookies:
                s.cookies.set(cookie['name'], cookie['value'])
            for u in range(1, 2):
                urls = self.start_url.format(u)
                res = s.get(urls, headers=headers)
                if res.status_code == 200:
                    html = res.text
                    return html
                else:
                    raise ConnectionError
        else:
            raise GetCookie

    def parse(self):
        html = etree.HTML(self.request())
        watch_type = html.xpath('//*[@id="hs-below-list-items"]/li/div/div[3]/h3/a/text()[1]')
        # print(watch_type)


if __name__ == '__main__':
    spider = WatchIndex()
    spider.parse()
