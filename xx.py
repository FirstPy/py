# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
import sys
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
class BaiDuTest(unittest.TestCase):
    #第一个测试
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.base_url='http://www.baidu.com'


    def test_baidu(self):
        #百度测试
        print("百度测试开始")
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("mahao")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title=driver.title
        print(title)
        self.assertEqual(title,u'马昊_百度搜索')
        driver.back()
        time.sleep(2)
        title1=driver.title
        print(title1)
        driver.refresh()
        size=driver.find_element_by_id('kw').size
        print (size)
        print("百度测试结束")

    def tearDown(self):
        self.driver.quit()

class Nba(unittest.TestCase):
    '''NBA测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.baidu.com'

    def test_nba(self):
        '''nba'''
        print("nba测试开始")
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("nba")
        driver.find_element_by_id("su").click()
        cookie=driver.get_cookies()
        print(cookie)
        print("nba测试结束")


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(BaiDuTest("test_baidu"))
    suite.addTest(Nba("test_nba"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    print"执行到了"
    #filename = r"D:\\jieguo.html"
    filename="D:\\result\\result"+now+".html"
    #filename = "./result" + now + ".html"
    #filename = "./result.html"
    fp=open(filename,'wb')


    #运行测试集合
    #runner=unittest.TextTestRunner()
    runner=HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')

    runner.run(suite)
    #fp.close()