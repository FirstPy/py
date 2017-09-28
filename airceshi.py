# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import  time
import  sys
reload(sys)
sys.setdefaultencoding('UTF-8')
class AirTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.base_url='http://boss.tuniu.org'
        self.url = 'http://boss.tuniu.org/ORD/ORD_order/view/orderFlightInquiry.html'



    def FlightTest(self):
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(3)
        self.driver.find_element_by_id('username').send_keys('mahao')
        self.driver.find_element_by_id('password').send_keys('mh19920812~')
        self.driver.find_element_by_name('submit').click()
        time.sleep(3)
        driver.get(self.url)
        title=driver.title
        print (title)
        self.assertEqual(title,u'机票预订')


    def setDown(self):
        self.driver.close()


if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(AirTest('FlightTest'))
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #unittest.main()



