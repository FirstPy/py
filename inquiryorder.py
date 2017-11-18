# -*- coding: utf-8 -*-
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
class AirInquiry(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        url=''

