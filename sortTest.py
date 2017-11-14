# -*- coding: utf-8 -*-
a=[3,34,2,123,67]
a.sort(key=int,reverse=True)
print a

b=['ada','dwdad','a','ds']
b.sort(key=len)
print b

info={"name":"mh"}
print info.get("age",'不存在')
print info.get('age')