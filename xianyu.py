#!/usr/bin/python
#-*- coding:utf8

import urllib,urllib2
from pyquery import PyQuery
import urlparse

keywords=['文曲星','电子词典']

def get_url(keyword):
    url = 'https://s.2.taobao.com/list/list.htm?st_edtime=1&ist=0&q=%s'%(urllib.quote(keyword.decode('utf8').encode('gbk')))
    return url

def process(soup):
    doc = PyQuery(url)
    item_info = doc('ul li div.item-info').eq(0)
    item_url = item_info('div.item-pic a').attr('href')
    r = urlparse.urlparse(item_url)
    item_id = urlparse.parse_qs(r.query)['id'][0]
    item_title = item_info('h4.item-title').text()
    item_price =  item_info('div.item-price span.price em').text()
    item_description = item_info('div.item-description').text()
    item_url = item_info('div.item-pic a').attr('href')
    print item_title,item_price,item_description,item_url,item_id
    

for keyword in  keywords:
    url = get_url(keyword)
    print url
    process(url)
