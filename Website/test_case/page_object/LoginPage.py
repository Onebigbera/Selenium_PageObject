# -*-coding:utf-8 -*-
# File :LoginPage.py
# Author:George
# Date : 2019/1/1
# motto: Someone always give up while someone always try!
"""
    单独的UI测试都可以是基于页面基类PageObject的子类
"""

from BasePage import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    """
    首页登陆页面相关的类-继承页面基类
    此处的'/'按照参数的作用域 LEGB 原则 对应在基类中的url
    """
    url = '/news/'

    """
        定位器 元祖形式封装,这是按照Empire页面上元素定位封装的这里为登陆输入定位器，当页面上元素改变时，只需要修改定位器即可 一改全改
    """
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME, 'Submit')

    def type_username(self, username):
        """
        函数中的 *self.username_loc 将元祖中的参数进行解包,这里的find_element 函数是 PageObject 中自己封装的函数
        :param username: username to type
        :return:
        """
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        """
        输入密码的函数 同样 *password_loc 也是具有解包功能
        :param password:
        :return:
        """
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        """
        点击登陆按钮
        :return:
        """
        self.find_element(*self.submit_loc).click()

    def Login_action(self, username, password):
        """
        封装登陆的方法，根据登陆之后页面元素的变化 依据此可以判断用户是否登陆成功
        :param username:
        :param password:
        :return:
        """
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    """
        定义登陆成功和登陆失败的定位器
    """
    loginPass_loc = (By.LINK_TEXT, "我的空间")
    loginFail_loc = (By.NAME, 'username')

    def type_loginPass_hint(self):
        """
        检查用户是否登陆成功，照样在参数中可以使用 *self.loginPass_loc定位器
        :return: 获取到定位器元素的文本, 用于断言判断，主要是用来做断言判断
        """
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        """
        根据已经设定了的登陆失败的定位器属性-文本做登陆失败判断断言，如果登陆失败，就会重新回到登陆页面 根据定位器得到的值为空
        :return:
        """
        return self.find_element(*self.loginFail_loc).text

