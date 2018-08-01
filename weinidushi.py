# -*- coding: UTF-8 -*- 
import os,sys
import urllib3
import requests
from lxml import etree
if len(sys.argv)>1:
    nb=sys.argv[1]
else:
    nb=None
http = urllib3.PoolManager()  # 创建请求
ret = http.request('GET', 'http://www.thepoemforyou.com/ruheshouting/2018niandebochudan/')  # 返回一个 HTTPResponse 对象
html = etree.HTML(ret.data)
if nb is None:
    result = html.xpath('//tr//a')[0].attrib["href"]
else:
    result = html.xpath('//tr//a')[int(nb)].attrib["href"]
mainpage = http.request('POST', result)  # 返回一个 HTTPResponse 对象
html = etree.HTML(mainpage.data)
result = html.xpath('//mpvoice')
dirmedia=result[0].attrib["voice_encode_fileid"]

filename = 'http://res.wx.qq.com/voice/getvoice?mediaid='+dirmedia
local="为你读诗/haha.mp3"
req = requests.get(filename)
with open(local, 'wb') as code:  
    code.write(req.content)
cmd="play "+local
os.system("play "+local)