# -*-coding:utf-8 -*-
# File :BasePage.py
# Author:George
# Date : 2019/1/1
# motto: Someone always give up while someone always try!
"""
    Page Object 类 将UI页面的元素和操作进行封装
"""
from time import sleep


class Page(object):
    """
    页面基础类/页面基类
    """

    url = ""
    def __init__(self, driver):
        """
        PageObject 的属性
        self.base_url: 根url| 页面基类的url
        :param driver:
        """
        self.base_url = r'http://localhost'
        self.driver = driver
        self.timeout = 10

    # 打开不同的子页面
    def _open(self, url):
        """
        _var private attr
        var_ to avoid conflict with keyword variant
        :param url: 子页面的对应路由 在各个继承基类的子类中定义
        :return:
        """
        url_ = self.base_url + url
        print("Test page is: %s" % url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)

        # assert  pattern assert expression [, option]
        assert self.driver.current_url == url_, 'Did not land on %s' % url_

    def open(self):
        """
        定义一个公有方法来调用私有方法 _open(),在_open()方法中需要传入子url，这个url会按照作用域范围去寻找，在LoginPage类中定义了 所以调用的时候不会报错
        self.url 其会在对应的页面中寻找
        :return:
        """
        self._open(self.url)

    def find_element(self, *loc):
        """
        最基本的定位器,可以完善 可以再写一个寻找多个元素的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)
