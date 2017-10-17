# -*- coding: utf-8 -*-
import urllib
bd=urllib.urlopen("http://baidu.com")
print bd.info()
print bd.getcode()
print bd.geturl()
for line in bd:
    print line,
bd.close()
