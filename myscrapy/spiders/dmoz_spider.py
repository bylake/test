# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:37:14 2016

@author: LiuNan
"""
#from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector
#from tutorial.items import DmozItem
#class DmozSpider(BaseSpider):
#   name = "dmoz"
#   allowed_domains = ["dmoz.org"]
#   start_urls = [
#       "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#       "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#   ]
#   def parse(self, response):
#       hxs = HtmlXPathSelector(response)
#       sites = hxs.select('//ul/li')
#       items = []
#       for site in sites:
#           item = DmozItem()
#           item['title'] = site.select('a/text()').extract()
#           item['link'] = site.select('a/@href').extract()
#           item['desc'] = site.select('text()').extract()
#           items.append(item)
#       return items
#from scrapy.spider import Spider  
#from scrapy.selector import Selector  
#  
#from tutorial.items import DmozItem  
#  
#class DmozSpider(Spider):  
#    name = "dmoz"  
#    allowed_domains = ["dmoz.org"]  
#    start_urls = [  
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
#    ]  
#  
#    def parse(self, response):  
#        sel = Selector(response)  
#        sites = sel.xpath('//ul[@class="directory-url"]/li')  
#        items = []  
#        for site in sites:  
#            item = DmozItem()  
#            item['title'] = site.xpath('a/text()').extract()  
#            item['link'] = site.xpath('a/@href').extract()  
#            item['desc'] = site.xpath('text()').extract()  
#            items.append(item)  
#        return items  

# -*- coding: utf-8 -*-
#from scrapy.selector import Selector
#import scrapy
#from scrapy.loader import ItemLoader, Identity
#from tutorial.items import MeizituItem
# 
# 
#class MeizituSpider(scrapy.Spider):
#    name = "meizitu"
#    allowed_domains = ["meizitu.com"]
#    start_urls = (
#        'http://www.meizitu.com/',
#    )
# 
#    def parse(self, response):
#        sel = Selector(response)
#        for link in sel.xpath('//h2/a/@href').extract():
#            request = scrapy.Request(link, callback=self.parse_item)
#            yield request
# 
#        pages = sel.xpath("//div[@class='navigation']/div[@id='wp_page_numbers']/ul/li/a/@href").extract()
#        print('pages: %s' % pages)
#        if len(pages) > 2:
#            page_link = pages[-2]
#            page_link = page_link.replace('/a/', '')    
#            request = scrapy.Request('http://www.meizitu.com/a/%s' % page_link, callback=self.parse)
#            yield request
# 
#    def parse_item(self, response):
#        l = ItemLoader(item=MeizituItem(), response=response)
#        l.add_xpath('name', '//h2/a/text()')
#        l.add_xpath('tags', "//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p")
#        l.add_xpath('image_urls', "//div[@id='picture']/p/img/@src", Identity())
# 
#        l.add_value('url', response.url)
#        return l.load_item()


#######


#coding=utf-8
from scrapy.spiders import Spider
import re
from myscrapy.items import MyscrapyItem
from scrapy.http.request import Request
# please pay attention to the encoding of info,otherwise raise error
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')


class download_douban(Spider):
    name = "download_douban"
    def __init__(self, url='152686895', *args, **kwargs):
        self.allowed_domains = ['douban.com']
        self.start_urls = [
                'http://www.douban.com/photos/album/%s/' %(url) ]
        #call the father base function
        self.url = url
        super(download_douban, self).__init__(*args, **kwargs)

    def parse(self, response):
        """
        :type response: response infomation
        """
        list_imgs = response.xpath('//div[@class="photolst clearfix"]//img/@src').extract()
        if list_imgs:
            item = DoubanImgsItem()
            item['image_urls'] = list_imgs
            yield item