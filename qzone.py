#-*- coding: utf-8 -*-
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
    headers={
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
	     'Accept': 'image/png,image/*;q=0.8,*/*;q=0.5',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	     'Cookie' : 'skey=@FRy5DAAcW; zzpaneluin=; zzpanelkey=; p_skey=2UMFO9hAbh7EbUrZSCMreWsqSN0BqDxxVZWlIeCjtns_; pt4_token=ihdi4sFI7yzFxr3Rd2lYO6epaS1JL*AyknpSa-EtMe8_; p_uin=o0386731845; pgv_pvi=5139627008; pgv_si=s7608884224; pgv_pvid=7421656560; pgv_info=ssid=s8439409521; pt2gguin=o0386731845; uin=o0386731845; RK=lfFHhsPWR0; qzone_check=386731845_1462244448; ptcz=02ecad39a63e5cbd58b23781da4ead461d761a5484e5d4e89ce91079656fbb22; randomSeed=918764; Loading=Yes'
            }
    r = requests.get(url,headers)
    print r.status_code
    print r.headers
    print r.content
      

  def start(self): 
    print "begin"
    self.enable = True
      
    self.LoadPage()
      
      


spider = my_spider()
spider.start()	
