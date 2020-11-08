import scrapy


class TableSpider(scrapy.Spider):
    name = 'table'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table = response.xpath('//table[contains(@class, "wikitable sortable")]')[0]
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
        	rank = tr.xpath('.//td[1]/text()').extract_first().strip()
        	city = tr.xpath('./td[2]//text()').extract_first()
        	state = tr.xpath('.//*[@class="flagicon"]/following-sibling::a/text()|''.//*[@class="flagicon"]/following-sibling::text()').extract_first().strip()
        	population_2019 = tr.xpath('./td[4]/text()').extract_first().strip()
        	census_2010 = tr.xpath('./td[5]/text()').extract_first().strip()
        	location = tr.xpath('.//span[@class="geo-dec"]/text()').extract()
        	yield{
        		'Rank' : rank,
        		'City' : city,
        		'State' : state,
        		'Population 2019' : population_2019,
        		'2010 census' : census_2010,
        		'Location' : location,
        	}

