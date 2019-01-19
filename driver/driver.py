# -*-coding:utf-8 -*-
# File :driver.py
# Author:George
# Date : 2019/1/2
# motto: Someone always give up while someone always try!
"""
    封装返回各种浏览器驱动的函数
"""
from selenium import webdriver
from time import sleep


from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options as FO


def browser():
    """
    定义各种浏览器驱动 包括无头浏览器PhantomJS
    :return:
    """
    # 常规模式
    # Chrome_driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')

    # 构造 Chrome 无头模式
    options = Options()
    # 添加无头参数
    options.add_argument("--headless")
    # 将构造参数添加进去
    Chrome_driver_headless = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe', options=options)

    # Firefox_driver = webdriver.Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe')

    # 构造Firefox无头浏览器
    # options = FO()
    # options.add_argument('--headless')
    # Firefox_driver_headless = Firefox(executable_path=r'E:\Installation_packages\Chrome_plugins\geckodriver.exe',options=options)

    # Ie_driver = webdriver.Ie(executable_path=r'E:\Installation_packages\Chrome_plugins\IEDriverServer.exe')

    """
        selenium 3中已经放弃使用Phantom JS 如果必须使用就需要将selenium降级到2版本；或者使用Chrome或者Firefox的无头模式
    """
    # driver = webdriver.PhantomJS(executable_path=r'E:\Installation_packages\Browser_Packages\Headless Browser\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    return Chrome_driver_headless


if __name__ == "__main__":
    url = r'https://www.baidu.com/'
    driver = browser()
    driver.get(url)
    sleep(10)
    print(driver.title)
    print(driver.current_url)
    driver.close()
    driver.quit()
