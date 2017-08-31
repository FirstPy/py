# -*- coding: utf-8 -*-

import  sys

import math

reload(sys)
sys.setdefaultencoding('UTF-8')
def dg_search(seg,number):
    if len(seg)>1:
        middle=len(seg)/2
        if middle>=1:
            if number>seg[middle]:
                dg_search(seg[middle+1:],number)
            elif number<seg[middle]:
                dg_search(seg[:middle],number)
            else:
                print ("您查找的数值为%s" %seg[middle])
        else:
            print('not found!')
    elif seg[0]==number:
        print ("您查找的数值为%s" % seg[0])
    else:
        print('not found!')


if __name__=='__main__':
    l=[4,56,78,23,77,12,2]
    l.sort()
    print l
    dg_search(l,4)



