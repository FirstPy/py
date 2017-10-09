# -*- coding: utf-8 -*-
def fibs(n):
    Fn=[0,1]
    for i in range(2,n):
        Fn.append(Fn[i-1]+Fn[i-2])
    print Fn
fibs(11)
