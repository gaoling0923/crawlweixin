# -*- coding: utf-8 -*-
import scrapy
import os
import subprocess

import time

import sys


class SpiderwxSpider(scrapy.Spider):
    name = 'spiderwx'
    allowed_domains = ['weixin.sogou.com']
    # start_urls = ['http://weixin.sogou.com/weixin?type=2&query=%E4%B8%80%E6%B1%BD%E5%A5%94%E8%85%BE&ie=utf8&s_from=input&_sug_=n&_sug_type_=&w=01015002&oq=&ri=0&sourceid=sugg&sut=605&sst0=1506307195407&lkt=1%2C1506307195305%2C1506307195305']
    start_urls = ['http://weixin.sogou.com/weixin?type=2&query=%E4%B8%80%E6%B1%BD%E5%A5%94%E8%85%BE&ie=utf8&s_from=input&_sug_=n&_sug_type_=&w=01015002&oq=&ri=0&sourceid=sugg&sut=605&sst0=1506307195407&lkt=1%2C1506307195305%2C1506307195305']

    def __init__(self):
        self.count=0;

    def loginParse(self,response):
        response.css('')


    def parse(self, response):
        print('1234')

        self.count = self.count + 1
        next = response.css('#sogou_next::attr(href)').extract_first();
        nurl = response.urljoin(next)  # urljoin
        print('下一页', nurl)
        print('计数：', self.count)
        # Request.
        yield scrapy.Request(nurl,callback=self.parse)

    def showQRImage(self):
        # global tip

        url = 'https://login.weixin.qq.com/qrcode/' + self.uuid
        params = {
            't': 'webwx',
            '_': int(time.time()),
        }
        print('url', url)

        response = self.session.get(url, params=params)

        self.tip = 1

        with open(self.QRImgPath, 'wb') as f:
            f.write(response.content)
            f.close()

        if sys.platform.find('darwin') >= 0:
            subprocess.call(['open', self.QRImgPath])
        elif sys.platform.find('linux') >= 0:
            subprocess.call(['xdg-open', self.QRImgPath])
        else:
            os.startfile(self.QRImgPath)

        print('请使用微信扫描二维码以登录')
