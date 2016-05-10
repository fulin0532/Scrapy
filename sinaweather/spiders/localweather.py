#coding=utf-8
import scrapy
from sinaweather.items import SinaweatherItem
class WeatherSpider(scrapy.Spider):
	name="myweather"
	allowed_domains=["sina.com.cn"]
	start_urls=["http://weather.sina.com.cn"]
	def parse(self,response):
		item=SinaweatherItem()
		item['city']=response.xpath('//h4[@id="slider_ct_name"]/text()').extract()
		item['date']=response.xpath('//p[@class="wt_fc_c0_i_date"]/text()').extract()
		item['dayDesc']=response.xpath('//img[@class="icons0_wt png24"]/@title').extract()
		item['dayTemp']=response.xpath('//p[@class="wt_fc_c0_i_temp"]/text()').extract()
		return item