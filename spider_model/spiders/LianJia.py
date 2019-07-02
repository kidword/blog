# -*- coding:utf-8 -*-
from spider_model.db.mydb import MySQL
from spider_model.http.request import Requests
from spider_model.conf.confs import *
from spider_model.db.redisdb import RedisQueue
import requests


class LjSpider:
    queue = RedisQueue()

    def __init__(self):
        self.start_url = 'http://www.baidu.com'

    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        weixin_request = Requests(url=self.start_url, callback=self.parse_index, need_proxy=True)
        self.queue.add(weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = response.text
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request = Requests(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.start_url + str(next)
            weixin_request = Requests(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def parse_detail(self, response):
        doc = response.text
        yield doc

    def request(self, weixin_request):
        if weixin_request.need_proxy:
            proxy = self.get_proxy()
            if proxy:
                proxies = {
                    'http': 'http://' + proxy,
                    'https': 'https://' + proxy
                }
                return self.session.send(weixin_request.prepare(),
                                         timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)



if __name__ == '__main__':
    sp = LjSpider()
    sp.start()
