# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import platform
import sys
from sys import exit, path
from datetime import date, timedelta
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 
from ScrapingHelpers import *

yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")


class FocusSpider(scrapy.Spider):
	name = "focus"
	start_urls = ['http://www.focus-news.net/news/Yesterday/']


	def __init__(self):

		cwd = os.getcwd()
		print 'Yesterday information will be collected. Date: %s'%(Yesterday)

		self.json_datafile = 'Reports/Focus-'+Yesterday+'.json'
		self.links_seen = self.get_ids(self.json_datafile)
		self.links_seen = set (map( lambda str: str[31:49], self.links_seen))	
		

	def get_ids(self, json_datafile):
		ids = []
		
		try:
			ids = read_ids(json_datafile)
		except (IOError,ValueError):
			return set(ids)
		return set(ids)

		
		
	def parse(self, response):

		# "Empty output file"
		fileName="Reports/Focus-%s.json"%(Yesterday)
		f = open(fileName, 'w').close()
	
		links=response.xpath('//div[@class="cnk-ttl"]/h2/a/@href').extract()
		links = list (map( lambda str: 'http://www.focus-news.net'+str[1:], links))		
		print 'links: %d'%(len(links))
		
		# for link in links:
			# if link[31:49] not in self.links_seen:
				# try:
					# print 'save data: %s'% link 
					# yield scrapy.Request(url=link, callback=self.parse_page)
				# except:
					# e = sys.exc_info()[1]
					# print "Error: %s" %(e)

		for link in links:
			yield scrapy.Request(url=link, callback=self.parse_page)

 	def parse_page(self, response):
		# 'We need the titles, links and times to index and follow'
		try:
			url   = response.url
			title = response.xpath('//div[@class="inside-top-title"]/h1/text()').extract_first().strip()
			article = u''.join(response.xpath('//div[@class="print-content font-resize-content"]/div[@class="inside-body-content jstf"]/text() | //div[@class="print-content font-resize-content"]/div[@class="inside-body-content jstf"]/b/text()').extract()).strip()

			pubDate=yesterday
			
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate
				}	

		except:
			print 'Error url:',url
