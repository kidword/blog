# -*- coding:utf-8 -*-
from requests import Request
from spider_model.conf.confs import *


class Requests(Request):
    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        Request.__init__(self, method, url, headers)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout

    # @classmethod
    # def request(cls, url, option={}):
    #     try:
    #         User_Agent = {'User-Agent': user_agent}
    #         headers = dict(User_Agent, **option)
    #         response = requests.get(url, headers=headers)
    #         if response.status_code == 200:
    #             return response.text
    #     except ConnectionError:
    #         logger.error("连接错误")
