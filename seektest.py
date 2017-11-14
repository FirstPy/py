# -*- coding: utf-8 -*-
x=file('D:\\aa.txt','r')
print x.tell()
x.seek(3)
print x.tell()
x.seek(5,1)
print x.tell()
x.seek(3,2)
print x.tell()