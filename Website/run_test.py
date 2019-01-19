# -*-coding:utf-8 -*-
# File :run_test.py
# Author:George
# Date : 2019/1/2
# motto: Someone always give up while someone always try!
"""
    管理其他的测试用例
"""
import unittest
from BSTestRunner import BSTestRunner
import time
from functionG import latest_report, send_mail


def run_test():
    report_dir = "./test_report"
    test_dir = "./test_case"

    print("Start run testcase...")
    # 获取测试用例py文件
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")

    # 字符串化时间
    now = time.strftime("%Y-%m-%d_%H_%M_%S")

    # 拼接生成测试汇报的路径
    report_name = report_dir + '/' + now + "result.html"

    with open(report_name, 'wb') as fw:
        runner = BSTestRunner(stream=fw, title="Test_report", description="Login_Test")
        runner.run(discover)
        fw.close()
    print("End test...")

    # 查找最新报告,获取到最新报告路径
    print("查找最新报告...")
    latest_report_file = latest_report(report_dir)

    # 邮件发送报告
    print("邮件发送测试报告...")
    send_mail(latest_report_file)
    print("邮件发送完成...")


if __name__ == "__main__":
    run_test()
