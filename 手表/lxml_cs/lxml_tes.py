# coding=utf-8

from Watch_ali.lxml_cs import lxml_xpath
from lxml import etree

html = etree.HTML(lxml_xpath.strs)
img_info = html.xpath("//div[@class='item']/div[@class='has-sku-image']/a/text()")  # 可选颜色  4 Colors Available
img_url = html.xpath("//div[@class='pic']/a/@href")
image_url = [i.replace("//", "") for i in img_url]    # 得到图片链接
content = html.xpath("//div[@class='info']/span[@class='separator']")   # 介绍内容
print(len(content))