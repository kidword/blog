import scrapy
from flight.items import FlightItem
from copy import deepcopy


class JdSpider(scrapy.Spider):
    name = 'country'
    start_urls = ['https://www.flightradar24.com/data/airports']

    def parse(self, response):
        table = response.xpath('//*[@id="tbl-datatable"]/tbody/tr/td[3]/a')
        for tr in table:
            item = {}
            if tr.xpath("./text()").extract_first() != None:
                L = tr.xpath("./text()").extract_first().replace("'", "")
                L1 = L.replace("(", "")
                L2 = L1.replace(")", "")
                L3 = L2.replace(",", "")
                L4 = L3.strip()
                L5 = L4.replace(" ", "-")
                item["name"] = L5
                item['href'] = "https://www.flightradar24.com/data/airports/"+item["name"]

                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_content,
                    meta={"item": deepcopy(item)}
                )

    def parse_content(self, response):
        item = response.meta["item"]
        table = response.xpath('//*[@id="tbl-datatable"]/tbody/tr')
        for tr in table:
            if tr.xpath("./td/a/@data-iata").extract_first() != None:
                item['airport'] = tr.xpath("./td/a/@title").extract_first()
                item['code'] = tr.xpath("./td/a/@data-iata").extract_first()
                item['lat'] = tr.xpath("./td/a/@data-lat").extract_first()
                item["lon"] = tr.xpath("./td/a/@data-lon").extract_first()
                data = FlightItem()
                data['name'] = item['name']
                data['airports'] = item['airport']
                data['code'] = item['code']
                data['lat'] = item['lat']
                data['lon'] = item["lon"]
                print(data)
                yield data




