# -*- coding: utf-8 -*-
import sys
from time import sleep,ctime
import threading

reload(sys)
sys.setdefaultencoding('UTF-8')
#音乐播放器
def music(func,loop):
    for i in range(loop):
        print ("I was listening to %s! %s" %(func,ctime()))
        sleep(2)
#视频播放器
def movie(func,loop):
    for i in range(loop):
        print("I was watching %s! %s" %(func,ctime()))
        sleep(5)

#创建线程数组
threads=[]

#添加到线程数组
t1=threading.Thread(target=music,args=('动力火车',2))
threads.append(t1)

t2=threading.Thread(target=movie,args=("战狼2",2))
threads.append(t2)

if __name__=="__main__":
#启动线程
    for t in threads:
        t.start()
    #守护线程
    for t in threads:
        t.join()
print("all end at %s" %ctime())

