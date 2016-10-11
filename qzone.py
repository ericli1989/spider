#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import string
import thread
import re

class my_spider:

  def __init__(self):
    self.page = 1
    self.pages = []
    self.enable = False
    #u"获取以第一页面，由于qzone的加密方式有点复杂，不想将时间耗在这个"
    #u"上面，第一个版本就不对加密方式进行处理，采取浏览器页面首次登陆"
    #u"后获取相应的cookie值，手动写入相应配置中，然后执行脚本进行页面"
    #u"抓取"
  
  def GetPage(self, url_prefix, qq_number,  header, feedstime):
    s = requests.Session()
    s.headers.update(header)
    r = s.get(url)
    print ""
    #print r.status_code
    #print r.headers
    #print r.content
    
    myItems = re.findall('ownerProfileSummary=\["(.*?)",\\s+(.*?),\\s+(.*?),\\s+"(.*?)",\\s+"(.*?)",\\s+"(.*?)",\\s+"(.*?)",\\s+"(.*?)"\],', r.content, re.S) 
    #myItems = re.findall('ownerProfileSummary=\["(.*?)"\],', r.content, re.S) 
    for items in myItems:
        name = items[0].strip()
        age = items[2].strip()
        address = items[3].strip()
        qzone_name = items[4].strip()
        birthday = items[6].strip()
        print name 
        print age
        print address
        print qzone_name
        print birthday 
		
 
    myItems = re.findall('homeAddr:{"hco":"(.*?)","hp":"(.*?)","hc":"(.*?)"}', r.content, re.S) 
    for item in myItems:
        country = item[0] 
        province = item[1] 
        city = item[2] 
        print country
        print province
        print city


	#获取好友信息，爬


	# \\s+   匹配任意连续空白( " ", "\n ", "\r ", "\t " 等) 
    temps = re.findall('feedstime:\'(.*?)\'(.*?)uin:\'(.*?)\'', r.content, re.S)
    for temp in temps:
    	feedstime=temp[0]
		temp_qq_number=temp[2]
		# 浏览页面滚动后数据信息
		another_url = "http://ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_act_all?uin=386731845&hostuin="+qq_number+"&scope=0&filter=all&flag=1&refresh=0&firstGetGroup=0&mixnocache=0&scene=0&begintime=undefined&icServerTime=&start=20&count=10&sidomain=ctc.qzonestyle.gtimg.cn&useutf8=1&outputhtmlfeed=1&refer=2&r=0.05353801200688568&g_tk="+g_tk
    	self.GetPage(url_prefix, qq_number, another_url, header, feedstime)
			 

	
 
 
    #myfriendNums = re.findall('qq_friendNum:"(.*?)"', r.content, re.S) 
    #print myfriendNums
    #for num in myfriendNums:
    #  friendnum = num
    #  print friendnum   
 
    #soup = BeautifulSoup(r.content)
    
    #print soup.findall("homeAddr")
    #for tag in soup.findall(re.compile("homeAddr")):
    #for tag in soup.findall(re.compile("homeAddr")):
    #  print(tag.name)
#    for link in soup.find_all('f-user-info')
#      i+=1
#      print i
#      print link
    
     

  def LoadStat(self):
    print u"请输入相应qq号码"
    qq_number = raw_input();
	url_prefix="http://user.qzone.qq.com/"
    print u"请输入qq号码对应的cookie值"
    qq_cookie = raw_input();
    print u"请输入qq号码对应的g_tk值"
    qq_cookie = raw_input();
	g_tk=raw_input();
    header={
	 	     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	     	 'Accept-Encoding': 'gzip, deflate',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
             'Connection': 'keep-alive',
            }
    header['Cookie'] = qq_cookie;
	#param: feedstime 说说发表时间
    #注意：登陆号码的qq空间和浏览他人的qq空间的格式不一致，需要区别分析
    feedstime='null'
	another_url='null'
    self.GetPage(url_prefix, qq_number, another_url, header, g_tk, feedstime)


  def start(self): 
    print "begin"
    self.enable = True
      
    self.LoadStat()
      
      


spider = my_spider()
spider.start()	
