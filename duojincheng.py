# -*- coding: utf-8 -*-
import sys
import multiprocessing
from time import ctime,sleep
reload(sys)
sys.setdefaultencoding("UTF-8")
def super_player(file,time):
    for i in range(2):
        print ("Starting playing %s! %s" %(file,ctime()))
        sleep(time)
lists={"动力.mp3":2,"喜欢你.mp3":3,"花好月圆.mp3":4}
mh=range(len(lists))
threads=[]
for file,time in lists.items():
    t=multiprocessing.Process(target=super_player,args=(file,time))
    threads.append(t)
if __name__=="__main__":
    for t in mh:
        threads[t].start()
    for t in mh:
        threads[t].join()
    print("end %s" %ctime())