# -*- coding: utf-8 -*-


'''
def print_params(x,y,z,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar
print_params(1,2,3,5,6,7,foo=1,bar=2)
print_params(1,2,4)


def add(x,y):
    return x+y

para=(1,2)
print add(*para)


def jieshen(n):
    if n==1:
        return 1
    else:
        return n*jieshen(n-1)

print jieshen(1)
print jieshen(5)
'''
seq = [34, 67, 8, 123, 4, 100, 95]
print len(seq)
seq.sort()
print seq
number = int(raw_input('数字：'))
start = 0
end = len(seq) - 1

while True:
    middle=int((start+end)/2)
    if seq[middle] > number:
        end=middle-1


    elif seq[middle] <number:
        start=middle +1

    elif seq[middle]==number:
        print "你要查找的数字在数组的第" + str(middle) + "个位置。"
        break
    if start>end:
        print '没有该数字。'
        break







