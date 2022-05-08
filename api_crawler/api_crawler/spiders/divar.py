import scrapy
import json


class DivarSpider(scrapy.Spider):
    name = 'divar'
    # allowed_domains = ['www.api.divar.ir']
    start_urls = ['https://api.divar.ir/v8/web-search/tehran/buy-apartment']
    time_stamp = None
    month = int()

    def parse(self, response):
        if DivarSpider.month > DivarSpider.time_stamp:
            result_dict = json.loads(response.body)
            # with open('divar.json', 'w') as json_file:
            #     json.dump(result_dict, json_file, ensure_ascii=False)
            homes = result_dict['widget_list']
            for home in homes:
                token = home['token']
                scrapy.Request(url=f'https://api.divar.ir/v5/posts/{token}')
            scrapy.Request(url=f'https://api.divar.ir/v8/web-search/tehran/buy-apartment', callback=self.parse)
        

        

