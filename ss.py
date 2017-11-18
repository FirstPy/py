# -*- coding: utf-8 -*-
import urllib2,urllib
import requests
import json
import base64
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
data={
  "responseId": "acc37070-cb6e-11e7-a978-d0431efba3d8",
  "groupIds": 1
}
#data=urllib.urlencode(data)
headers={"Content-Type":"application/json"}
#将数据变为json格式
#data=urllib.urlencode(data)
data=json.dumps(data)
print data
data=base64.b64encode(data)
print data

url1='http://10.10.31.19:10127/ase/query/split/detail'
'''
url2=urllib2.Request(url1,data)
response=urllib2.urlopen(url2)
print response.getcode()
apicontent=response.read()
print apicontent
'''
#r = requests.post('http://10.10.31.19:10127/ase/query/split/detail',
#                  data=data)
#print base64.b64decode(r.text)

r=requests.post(url=url1,data=data,headers = headers)
#print r.text
result=base64.b64decode(r.text)
print(result)
print(r.status_code)