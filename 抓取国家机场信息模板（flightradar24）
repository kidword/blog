from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
browser=webdriver.Chrome()
browser.get("https://www.flightradar24.com/data/airports/myanmar-burma")
#得到所有国家名称
lis=browser.find_elements_by_css_selector("#tbl-datatable > tbody > tr> td> a")

#列表去除'' ,并且添加到lis_new中
new_lis = []
ph_lis = []
for i in lis:
    if len(i.text)>=1:
        # 获取机场名称
        flight_name = i.get_attribute('title')
        # 获取中国机场名称
        city = i.text
        # 获取机场号码
        ph = i.get_attribute('data-iata')
        # 得到经度
        jindu = i.get_attribute('data-lat')
        # 得到纬度
        weidu = i.get_attribute('data-lon')
        lis1 = [flight_name,ph,jindu,weidu]
        new_lis.append(lis1)
        ph_lis.append(ph)
print(ph_lis)
print(new_lis)
#写入csv文件
name = ['F_code(起飞机场)', 'A_code（到达机场）', 'ar_lat（经度）', 'ar_lon（纬度）']
text = pd.DataFrame(columns=name,data=new_lis)
text.to_csv('D:\缅甸机场数据.csv')
#browser.close()
