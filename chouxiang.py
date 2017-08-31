# -*- coding: utf-8 -*-

def fib(num):
    result=[0,1]
    for i in range(num):
        result.append(result[-2] + result[-1])
        print i
    return result

print fib(10)
