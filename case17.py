# -*- coding: utf-8 -*-
import string
a=raw_input('输入的字符串为：')
yc=0
kc=0
sc=0
qc=0
print a
#b=len(a)
#print b
for i in a:
    if i.isalpha():
        yc +=1
    elif i.isspace():
        kc+=1
    elif i.isdigit():
        sc+=1
    else:
        qc+=1
print("英文个数为：%d；空格个数为：%d；数字个数为：%d；其他个数为：%d" %(yc,kc,sc,qc))

