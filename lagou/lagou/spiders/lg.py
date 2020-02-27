# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LgSpider(CrawlSpider):
    name = 'lg'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    rules = (
        Rule(LinkExtractor(allow=r'search.51job.com/list/'),  follow=True),
        Rule(LinkExtractor(allow=r'beijing'), callback='parse_job', follow=False),
    )

    def parse_job(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        a = response.xpath("//h1/text()").getall()
        b = response.xpath('//div/div/div/div/strong/text()').get()

        print(a,b)
        # return item
