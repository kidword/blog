# encoding=utf-8
import requests
import time
from selenium import webdriver
import random


driver = webdriver.Chrome()


def get_cookie_from_ali_cn():
    driver.get("https://login.aliexpress.com")   # 开始url
    time.sleep(3)
    try:
        login_frame = driver.find_element_by_id('alibaba-login-box')  # 定位frame元素
        driver.switch_to.frame(login_frame)
        driver.find_element_by_id('fm-login-id').send_keys('')
        time.sleep(random.randint(1, 3))
        driver.find_element_by_id("fm-login-password").send_keys('')
        time.sleep(random.randint(1, 3))
        driver.find_element_by_class_name('password-login').click()
        time.sleep(random.randint(1, 3))
    except Exception as e:
        print("登录失败...")
        raise e


def get_cookie():
    get_cookie_from_ali_cn()
    s = requests.Session()
    cookies = driver.get_cookies()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    driver.quit()
    url = 'https://www.aliexpress.com/wholesale?site=glo&g=y&SearchText=women+watches&page=1'
    resp = s.get(url)
    print(resp.text)

get_cookie()

driver.quit()


