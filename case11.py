# -*- coding: utf-8 -*-
a=[1,1]
def Ru(n):
    for i in range(2,n):
        a[i]=a[i-1] + a[i-2]
        a.append(a[i])
    print("第%d个月的兔子数为：%d" %(n,a[n-1]))

Ru(6)

