# -*- coding: utf-8 -*-
year=int(raw_input("输入的年份是："))
month=int(raw_input("输入的月份是："))
date=int(raw_input("输入的日期是："))
months=(0,31,59,90,120,151,181,212,243,273,304,335)
if(year>0):
    if(0 < month < 13):
        if(0 < date < 32):
            i = 0
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                i = 1
                if (i == 1 and month > 1):
                    num = months[month - 1] + date + 1
                else:
                    num = months[month - 1] + date
            else:
                num=num = months[month - 1] + date
            print("输入的日期为第%d天" % num)

        else:
            print("您输入日期不对！")
    else:
        print("您输入月份不对！")
else:
    print("您输入年份不对！")





