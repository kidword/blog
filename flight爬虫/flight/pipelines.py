# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class FlightPipeline(object):
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='localhost', user='root',
                                    password='hh226752', db='flightradar24', charset='utf8')

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        sql = "insert into world_copy(Countries,Airports_name,Airports_code,Airports_ar_lat,Airports_ar_lon)" \
              " VALUES (%s,%s,%s,%s,%s)"
        c = self.conn.cursor()
        c.execute(sql, (item['name'], item['airports'], item['code'], item['lat'], item['lon']))
        self.conn.commit()
        return item
