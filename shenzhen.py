#!/usr/bin/python
#-*- coding:utf8

import urllib,urllib2
from pyquery import PyQuery
import urlparse
import itchat
import time
import os.path

keywords=['']
UserName = '@98d290ab92f3aec018afa92c2ec0521d'

def get_url(keyword):
    url = 'https://s.2.taobao.com/list/list.htm?start=799&end=1500&st_edtime=1&ist=0&divisionId=440305&userId=0&catid=57194001&q='
    return url

def check(id):
    ID_FILE_NAME='id_list_shenzhen.txt'
    if os.path.exists(ID_FILE_NAME) == False:
        id_list= ['1']
        open(ID_FILE_NAME,'w').write(repr(id_list))
    id_list = open(ID_FILE_NAME).read()
    id_list = eval(id_list)

    if id in id_list:
        return False
    
    id_list.append(id)
    open(ID_FILE_NAME,'w+').write(repr(id_list))
    return True

def process(url):
    doc = PyQuery(url)
    item_info_list = doc('ul li div.item-info') 
    for item_info in item_info_list:
        item_info = doc('ul li div.item-info').eq(0)
        item_url = item_info('div.item-pic a').attr('href')
        r = urlparse.urlparse(item_url)
        item_id = urlparse.parse_qs(r.query)['id'][0]
        if check(item_id) == False:
            continue
        item_title = item_info('h4.item-title').text()
        item_price =  item_info('div.item-price span.price em').text()
        item_description = item_info('div.item-description').text()
        item_url = item_info('div.item-pic a').attr('href')
        msg="%s \n%s \n%s \nhttps:%s"%(item_title,item_price,item_description,item_url)
        print msg
        itchat.send(msg,toUserName=UserName)

def chat_login():
    global UserName

    itchat.auto_login()
    UserName = itchat.search_chatrooms(u'华哥快餐店')[0]['UserName']

    print UserName

    
def main():
    chat_login()
    while 1:
        for keyword in  keywords:
            url = get_url(keyword)
            # print url
            process(url)
        time.sleep(10)


if __name__ == '__main__':
    main()
