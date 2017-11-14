# -*- coding: utf-8 -*-
Sn=100.0
Hn=Sn/2
for k in range(2, 11):
    Sn+=2*Hn
    Hn=Hn/2

print Sn,Hn
print type(Hn)