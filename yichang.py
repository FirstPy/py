# -*- coding: utf-8 -*-
import exceptions
try:
    x=int(raw_input('enter the first number:'))
    y=int(raw_input('enter the second number:'))
    print x/y
except ZeroDivisionError:
    print("the second number can't be zero")