# -*-coding:utf-8 -*-
# File :function.py
# Author:George
# Date : 2019/1/2
# motto: Someone always give up while someone always try!
"""
    常见功能的封装 截图、邮件发送、获取最新测试报告
"""
import os
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def insert_img(driver, filename):
    """
    截图函数
    :param driver: 传入的驱动
    :param filename: 生成的文件名称
    :return:
    """
    # 获取当前文件所在路径
    func_path = os.path.dirname(__file__)
    print("当前文件的目录为:%s" % func_path)

    # 一直向上寻找，直到和test_report同级目录
    base_dir = os.path.dirname(func_path)
    print("当前文件目录的上级目录为:%s" % base_dir)

    # 字符串化处理 + 将路径中"\\"(绝对路径) 替换为"/"(相对路径)
    base_dir = str(base_dir)
    base_dir.replace("\\", "/")

    base = base_dir.split("/Website")[0]
    print(base)

    # 拼接截图文件的保存路径
    filepath = base + "/Website/test_report/screenshot/" + filename
    img_status = driver.get_screenshot_as_file(filepath)
    print(img_status)


def send_mail(latest_report):
    """
    将最近生成的测试报告发送的函数
    :param latest_report:最近生成文件的路径
    :return:
    """
    fr = open(latest_report, "rb")
    mail_content = fr.read()
    fr.close()

    smtpServer = "smtp.163.com"

    account = "onebigbera@163.com"
    password = "george9527"

    sender = "onebigbera@163.com"
    receiver = "onebigbera@163.com"

    subject = "Web Selenium自动化测试报告"
    msg = MIMEText(mail_content, "html", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    smtp = smtplib.SMTP_SSL(smtpServer, 465)
    smtp.helo(smtpServer)
    smtp.ehlo(smtpServer)
    smtp.login(account, password)
    try:
        print("开始发送邮件...")
        smtp.sendmail(sender, receiver, msg.as_string())
    except BaseException as e:
        print(e)
    print("邮件发送完成...")


def latest_report(report_dir):
    """
    在汇报目录下寻找最新的测试报告的函数
    :param report_dir:
    :return: 返回最近生成文件的路径
    """
    lists = os.listdir(report_dir)
    # lambda 函数返回的是report_dir目录下文件fn的创建时间 sort 函数中按照key=time进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    print("最近生成的汇报文件为:%s" % lists[-1])

    # 用 os.path.join()方法将最近生成文件的路径拼接起来
    file = os.path.join(report_dir, lists[-1])
    print("最近生成的文件路径为: %s" % file)
    return file


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    driver.get("http://www.sogou.com/")
    insert_img(driver, "sogou3.png")
    # latest_report(r'F:\Testing_Development\UnittestProjects\PageObject_unittest\Website\test_report\screenshot')
    # send_mail()
    # send_mail(r'F:\Testing_Development\UnittestProjects\PageObject_unittest\Website\test_data\test.html')
    pass
