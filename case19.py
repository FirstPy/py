# -*- coding: utf-8 -*-
for j in range(2,1001):
    Sn = []
    for k in range(1,j):
        if j%k==0:
            Sn.append(k)

    if(j==reduce(lambda x,y:x+y,Sn)):
        print j
        print Sn




