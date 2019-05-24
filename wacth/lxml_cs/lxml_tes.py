# coding=utf-8

from wacth.lxml_cs import lxml_xpath
from lxml import etree

html = etree.HTML(lxml_xpath.strs)
img_info = html.xpath("//div[@class='item']/div[@class='has-sku-image']/a/text()")  # 可选颜色  4 Colors Available
img_url = html.xpath("//div[@class='pic']/a/@href")
image_url = [i.replace("//", "") for i in img_url]    # 得到图片链接
content = html.xpath("//*[@id='hs-below-list-items']/li[1]/div/div[3]/h3/a/text()[1]/text()")   # 介绍内容
print(content)


