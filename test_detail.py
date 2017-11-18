# -*- coding: utf-8 -*-
import urllib2,urllib
import requests
import json
import base64
import sys
import json
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
class test_detail(unittest.TestCase):
    def setUp(self):
        print("test start")
        pass

    def tearDown(self):
        print("test end")
        pass
    def test_detail(self):
        self.data={
  "responseId": "7755b686-cc2d-11e7-a2f9-d0431efba3d8",
  "groupIds": 1
}
#data=urllib.urlencode(data)
        self.headers={"Content-Type":"application/json"}
#将数据变为json格式
#data=urllib.urlencode(data)
        data=json.dumps(self.data)
        print data
        data=base64.b64encode(data)
        print data

        self.url1='http://10.10.31.19:10127/ase/query/split/detail'
        r = requests.post(url=self.url1, data=data, headers=self.headers)
        result = base64.b64decode(r.text)
        print(result)
        print(r.status_code)
        self.assertIn("true",result)

if __name__ == '__main__':
    unittest.main()
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


#print r.text
