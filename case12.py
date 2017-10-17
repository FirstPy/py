# -*- coding: utf-8 -*-
from math import sqrt
def Zs(x,y):
    k=1
    h=0
    for i in range(x,y):
        for j in range(2,int(sqrt(i))+1):
            if(i%j ==0):
                k=0
                break
        if k==1:
            print i
            h=h+1
        k=1
    print("%d-%d素数总数为：%d"  %(x,y,h))

Zs(2,201)
