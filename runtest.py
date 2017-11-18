# -*- coding: utf-8 -*-
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import  test_inquiry
import test_detail

#构造测试集
suite=unittest.TestSuite()   #实例化
#TestSuite类的addTest()方法把不同测试类中的测试方法组装到测试套件中。
#增加测试用例==》接口文件名.接口类(方法也就是这个接口的其他用例),要把每一个测试用例都增加进来！！！
suite.addTest(test_inquiry.test_list("test_inquiry"))
suite.addTest(test_detail.test_detail("test_detail"))

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(suite)
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    print"执行到了，完美！"
    filename = "D:\\result\\air" + now + ".html"
    fp = open(filename, 'wb')
    #运行测试集合
    runner = HTMLTestRunner(stream=fp, title=u'机票查询列表详情测试报告', description=u'用例执行情况：')
    runner.run(suite)
    fp.close()
