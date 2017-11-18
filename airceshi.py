# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import  time
from HTMLTestRunner import HTMLTestRunner
import  sys
reload(sys)
sys.setdefaultencoding('UTF-8')
class AirInquiryTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.base_url='http://boss.tuniu.org'
        self.url = 'http://boss.tuniu.org/ORD/ORD_order/view/orderFlightInquiry.html'



    def FlightInquiryTest(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(3)
        self.driver.find_element_by_id('username').send_keys('mahao')
        self.driver.find_element_by_id('password').send_keys('Mh19920812')
        self.driver.find_element_by_name('submit').click()
        time.sleep(3)
        driver.get(self.url)
        title=driver.title
        print (title)
        self.assertEqual(title,u'机票预订')
        self.driver.maximize_window()
        now_handle=driver.current_window_handle   #获取当前窗口句柄
        print now_handle  # 输出当前获取的窗口句柄
        self.driver.find_element_by_id('orgCity').click()
        self.driver.find_element_by_xpath('html/body/div[2]/div[2]/ul[1]/li[1]/a').click()
        self.driver.find_element_by_id('dstCity').click()
        self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul[1]/li[2]/a').click()
        self.driver.find_element_by_id('date').clear()
        self.driver.find_element_by_id('date').send_keys('2017-11-26')
        self.driver.find_element_by_id('onewaySearch').click()
        time.sleep(5)
        #self.assertEqual(self.driver.find_element_by_xpath("//*[@class='tngpContainer']/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/div/strong"),u'选择','对比失败')
        self.driver.find_element_by_xpath("//*[@class='tngpContainer']/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/div/strong").click()
        time.sleep(3)
        #self.driver.maximize_window()

        all_handles = driver.window_handles  # 获取所有窗口句柄
        for handle in all_handles:
            if handle!=now_handle:
                print handle
                driver.switch_to_window(handle)
                select = self.driver.find_element_by_name('payMethod')
                select.find_element_by_xpath("//option[@value='2']").click()
                self.driver.find_element_by_id('memberIdInput').send_keys('63960842')
                #self.driver.find_element_by_name('contactName').send_keys('测试')
                #self.driver.find_element_by_id('contactTel').send_keys('17372203985')id('passangers')
                #self.driver.find_element_by_xpath("//*[@id='passangers']/table/tbody/tr[1]/td[1]/input").send_keys('mahao')
                #self.driver.find_element_by_name('psptId').send_keys('420528199009095011')
                self.driver.find_element_by_name('touristName').send_keys(u'马浩')
                self.driver.find_element_by_name('psptId').send_keys('420528199009095011')
                self.driver.find_element_by_id('submitId').click()

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(AirInquiryTest('FlightInquiryTest'))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    print"执行到了，完美！"
    filename = "D:\\result\\result" + now + ".html"
    fp = open(filename, 'wb')
    #运行测试集合
    #runner=unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp, title=u'国内机票查询测试报告', description=u'用例执行情况：')
    runner.run(suite)
    fp.close()





