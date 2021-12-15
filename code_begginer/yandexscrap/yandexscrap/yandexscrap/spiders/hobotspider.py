import scrapy
from scrapy.http.request import Request

# headers = {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
headers = {'user_agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}



class HobotSpider(scrapy.Spider):
    name = 'Hobot'
    headers = {'user_agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    start_urls = ['https://market.yandex.ru/catalog--pylesosy-i-aksessuary/75696/list?glfilter=7893318%3A14259474&hid=16126061&onstock=0&local-offers-first=0', "headers=headers"]


    def parse(self, response):
        
        for products in response.css("div._2vVOc"):
            try:
                yield {
                    'name': products.css('a._2f75n._24Q6d.cia-cs::text').get(),
                    'price': products.css('div._3NaXx._33ZFz._2m5MZ').replace('₽', ''),
                    'link': products.css('a._2f75n._24Q6d.cia-cs').attrib['href'],
            }
            except:
                yield {
                    'name': products.css('a._2f75n._24Q6d.cia-cs::text').get(),
                    'price': 'sold out',
                    'link': products.css('a._2f75n._24Q6d.cia-cs').attrib['href'],
                }
