# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from scrapy import signals

class JavaScriptMiddleware(object):

    def process_request(self, request, spider):
        print('rrrrr')
        if spider.name in ("spiderwx"):
            print("execute PhantomJS spiderName", spider.name);
            print("PhantomJS is starting...")
            driver = webdriver.PhantomJS() #指定使用的浏览器
            # driver = webdriver.Chrome() #指定使用的浏览器
            driver.get(request.url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            driver.current_window_handle
            time.sleep(3)
            body = driver.page_source
            print ("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return
class CrawlweixinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
