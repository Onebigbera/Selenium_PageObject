# -*-coding:utf-8 -*-
# File :test_login.py
# Author:George
# Date : 2019/1/2
# motto: Someone always give up while someone always try!
"""
    测试登陆的类 测试对象就是继承BasePage的Loginpage的类,依照参照元素结合断言进行判断
    PO 将元素定位和页面操作对象分层封装，解耦便于操作和维护
    如果是测试登陆 就在写一个 test_register用例
"""
from models import myunit
from functionG import insert_img
from page_object.LoginPage import LoginPage
from time import sleep
import unittest


class LoginTest(myunit.StartEnd):
    """
    测试登陆相关的类
    """

    # @unittest.skip("Just skip...")
    def test_login1_normal(self):
        """username password is normal"""
        print("test_login1_normal is start run...")
        po = LoginPage(self.driver)
        po.Login_action("george", "kaige1992")
        sleep(5)
        self.driver.get_screenshot_as_file(r'F:\Testing_Development\UnittestProjects\PageObject_unittest\Website\test_report\screenshot' + "\\test.png")

        # 断言与截屏
        self.assertEqual(po.type_loginPass_hint(), "我的空间")
        # 截图失败
        # insert_img(self.driver, "login_normal.png")
        print("test_login1_normal test end...")

    @unittest.skip("Just skip...")
    def test_login2_passwdError(self):
        """username is ok, passwd is error!"""
        print("test_login2_passwdError is start run...")
        po = LoginPage(self.driver)
        po.Login_action("george", "123456")
        sleep(5)

        # 断言与截图 登陆失败时按照定位器得到的值为""
        self.assertEqual(po.type_loginFail_hint(), '')
        insert_img(self.driver, "login2_fail.png")
        print("test_login2_passwdError test end...")

    @unittest.skip("Just skip...")
    def test_login3_empty(self):
        """username and password are empty"""
        print("test_login3_empty is start run...")
        po = LoginPage(self.driver)
        po.Login_action("", "")
        sleep(4)

        # 断言与截图
        self.assertEqual(po.type_loginFail_hint(), "")
        insert_img(self.driver, "login3_empty.png")
        print("test_login3_empty test end...")


if __name__ == "__main__":
    unittest.main()
