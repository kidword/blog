# encoding=utf-8
from lxml import etree
from watch import model_html
import re

html = etree.HTML(model_html.strs)
img_info = html.xpath("//div[@class='item']/div[@class='has-sku-image']/a/text()")  # 可选颜色  4 Colors Available
img_url = html.xpath("//div[@class='pic']/a/@href")
image_url = [i.replace("//", "") for i in img_url]  # 得到图片链接

watch_type = html.xpath('//*[@id="hs-below-list-items"]/li/div/div[3]/h3/a/text()[1]')
s = html.xpath('//*[@id="hs-below-list-items"]/li/div/div[3]/h3/a/font[1]/b/text()')

div = html.xpath('//*[@id="hs-below-list-items"]/li/div/div[3]')
s_lis = []
q_lis = []
for i in div:
    s = i.xpath('h3/a/font[1]/b/text()')
    q = i.xpath('/h3/a/text()[1]')
    if len(s) < 1:
        s.append('null')
    s_lis.append(s)
    q_lis.append(q)
print(len(q_lis))
# print(len(s))
