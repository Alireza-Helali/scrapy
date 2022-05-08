import scrapy


class WorldSpider(scrapy.Spider):
    name = 'world'
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath('//*[@id="example2"]/tbody/tr')
        for country in countries:
            country_name = country.xpath('.//td[2]/a/text()').get()
            link = country.xpath('.//td[2]/a/@href').get()

            yield response.follow(url=link, callback=self.parse_country, meta={'name': country_name})

    def parse_country(self, response):
        country = response.meta.get('name')
        rows = response.xpath(
            '//div[5]/table/tbody/tr')
        print(rows)
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[3]/text()').get()


            yield {
                'country_name': country,
                'year': year,
                'population': population
            }
