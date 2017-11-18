# -*- coding: utf-8 -*-
import requests
import json
import base64
import urllib
import unittest
class test_list(unittest.TestCase):
    def setUp(self):
        print("test start")
        pass
    def tearDown(self):
        print("test end")
        pass
    def test_inquiry(self):
        self.url='http://10.10.31.19:10127/ase/query/split/list'
        self.headers={"Content-Type":"application/json"}
        self.data= {
        "ver": "CAL600",
        "debug": "false",
        "passengers": {
            "count": 1,
            "psgType": "ADT"
        },
        "sid": "C01B01",
        "systemId": 52,
        "withTransfer": "true",
        "voyType": "ST",
        "voys": [
            {
                "orgCity": "SHA",
                "dstCity": "SHE",
                "deptDate": "2017-11-24"
            }
        ]
    }
        data=json.dumps(self.data)
        data=base64.b64encode(data)
        print data


    #print data

    #a=base64.b64encode(data)
    #print('入参位：%s' %a)

        r=requests.post(url=self.url,data=data,headers = self.headers)
        print r.text
        result=base64.b64decode(r.text)
        print(result)
        print(r.status_code)
        self.assertIn("true",result)
        self.assertDictEqual()



if __name__ == '__main__':
    unittest.main()