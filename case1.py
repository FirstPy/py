# -*- coding: utf-8 -*-
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                count=count+1
                print i,j,k

print("共组成数字个数为：%d" %count)