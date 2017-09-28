# -*- coding: utf-8 -*-
i=int(raw_input("当月利润为："))
jj=0
if (i <=100000):
    jj=int(i*0.1)
    print jj
elif(100000<i<200000):
    jj=100000*0.1+(i-100000)*0.075
    print jj


