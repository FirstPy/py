# -*- coding: utf-8 -*-
Sn=[]
c=0
n=int(raw_input('输入的数字是：'))
a=int(raw_input('相加的个数是：'))
for i in range(a):
    c=n+10*c
    Sn.append(c)
print Sn

sums=reduce(lambda x,y:x+y,Sn)
print sums
