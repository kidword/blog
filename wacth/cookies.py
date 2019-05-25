# encoding=utf-8
import requests
import time
from watch import conf
from selenium import webdriver
import random


class GetCookie:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.User_Agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 " \
                          "(KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        self.start_url = 'https://login.aliexpress.com'

    def get_cookie_from_ali_cn(self, username, pdw):
        self.driver.get(self.start_url)  # 开始url
        time.sleep(3)
        try:
            login_frame = self.driver.find_element_by_id('alibaba-login-box')  # 定位frame元素
            self.driver.switch_to.frame(login_frame)
            self.driver.find_element_by_id('fm-login-id').send_keys(username)
            time.sleep(random.randint(1, 3))
            self.driver.find_element_by_id("fm-login-password").send_keys(pdw)
            time.sleep(random.randint(1, 3))
            self.driver.find_element_by_class_name('password-login').click()
            time.sleep(random.randint(1, 3))

        except Exception as e:
            print("登录失败...")
            raise e

    def get_cookie(self):
        u_info = conf.user_info
        cookie_lis = []
        for u in u_info:
            self.get_cookie_from_ali_cn(u['email'], u['pwd'])
            cookies = self.driver.get_cookies()
            self.driver.quit()
            cookie_lis.append(cookies)
        return cookie_lis


if __name__ == '__main__':
    spider = GetCookie()
    spider.get_cookie()
