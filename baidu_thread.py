# -*- coding: utf-8 -*-
from threading import Thread
from selenium import webdriver
from time import sleep,ctime
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
def test_baidu(browser,search):
    print("start:%s" %ctime())
    print("browser:%s" %broswer)
    if browser=="ie":
        driver=webdriver.Ie()
    elif browser=='ff':
        driver=webdriver.Firefox()
    elif browser=='chrome':
        driver=webdriver.Chrome()
    else:
        print("参数有误")

    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()

if __name__=='__main__':
    lists={'ff':'Firefox','ie':'explorer','chrome':'谷歌'}
    files=range(len(lists))
    threads=[]
    for broswer,search in lists.items():
        t=Thread(target=test_baidu,args=(broswer,search))
        threads.append(t)
    for t in files:
        threads[t].start()
    for t in  files:
        threads[t].join()
    print ("THE END:%s" %ctime())



