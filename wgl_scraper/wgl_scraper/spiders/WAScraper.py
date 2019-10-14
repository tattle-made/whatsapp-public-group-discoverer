# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from wgl_scraper.items import ScraperItem
import time 


class WascraperSpider(CrawlSpider):
    name = 'wgl'
    allowed_domains = ['whatsappgrouplinks.org']
    start_urls = [
        'https://www.whatsappgrouplinks.org',
    ]
    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                deny=('/2018/08/porn-whatsapp-group-join-links.html',
                       '/2018/09/join-sex-whatsapp-group-links-list.html',
                        '/2018/08/adult-whatsapp-group-links.html',
                        '/2018/08/join-hot-whatsapp-group-links-list.html',
                        '/2018/08/join-girls-dating-whatsapp-group-links-list.html',
                        '/2018/09/join-desi-auntys-whatsapp-group-links-list.html',
                        '/2018/08/join--lesbian-whatsapp-group-links-list.html',
                        '/2018/08/gay-whatsapp-group-join-links.html',
                        '/2019/01/join-nonveg-whatsapp-group-links-list.html',
                        '/2018/09/join-18-whatsapp-group-links-list.html',
                        '/2018/08/love-whatsapp-group-links.html'),
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    def parse_items(self, response):
        items = []

        for group in response.xpath('//a/@href').re(r'https://chat.whatsapp.com/.*'):
                #print("printing group")
                #print(group)
                temp_item = ScraperItem()
                temp_item["group"] = group
                temp_item["source"] = response.url
                items.append(temp_item)
                    
        return items
