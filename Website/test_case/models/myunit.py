# -*-coding:utf-8 -*-
# File :myunit.py
# Author:George
# Date : 2019/1/2
# motto: Someone always give up while someone always try!
"""
    封装unittest中的每个测试用例setUp()和tearDown()方法
"""
import unittest
from driver import browser


class StartEnd(unittest.TestCase):
    """ 定义每个测试方法的准备和结束设置"""

    def setUp(self):
        """
        初始化driver, 可以设置连接数据库
        :return:
        """
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        """
        每个测试方法结束后的设置，比如关闭数据库
        :return:
        """
        self.driver.quit()
