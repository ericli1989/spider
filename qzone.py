#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import string
import thread


class my_spider:



  def __init__(self):
    self.page = 1
    self.pages = []
    self.enable = False
    
    #u"获取以第一页面，由于qzone的加密方式有点复杂，不想将时间耗在这个"
    #u"上面，第一个版本就不对加密方式进行处理，采取浏览器页面首次登陆"
    #u"后获取相应的cookie值，手动写入相应配置中，然后执行脚本进行页面"
    #u"抓取"
   

  def LoadPage(self):
    print u"请输入相应qq号码"
    qq_number = raw_input();
    url="http://user.qzone.qq.com/"+qq_number
    print url
    print u"请输入qq号码对应的cookie值"
    qq_cookie = raw_input();
    header_temp={
	     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	     'Accept-Encoding': 'gzip, deflate',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
             'Connection': 'keep-alive',
            }
    header_temp['Cookie'] = qq_cookie;
    s = requests.Session()
    s.headers.update(header_temp)
    r = s.get(url)
    print ""
    print r.status_code
    print r.headers
    #print r.content
    i = 0
    soup = BeautifulSoup(r.content)
    for link in soup.find_all('f-user-info')
      i+=1
      print i
      print link
	

  def start(self): 
    print "begin"
    self.enable = True
      
    self.LoadPage()
      
      


spider = my_spider()
spider.start()	
