# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: run_all_case.py
# @time: 2020/5/8 21:37
# @desc
import os
from common.excel_utills import config
from common import HTMLTestReportCN
import unittest
from common.email_utils import EmailUtiles

current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, config.case_path)
report_path = os.path.join(current_path, config.report_path)


class RunAllCase:
    def __init__(self):
        self.case_path = case_path
        self.report_path = report_path
        self.title = '禅道自动化测试报告-PY'
        self.description = 'UI_TEST'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.case_path, pattern='*_test.py', top_level_dir=self.case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        # 设置测试报告路径
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)

        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')

        fb = open(report_path, "wb")
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fb, title=self.title, description=self.description, tester='new')
        runner.run(all_suite)
        fb.close()
        return dir_path


if __name__ == '__main__':
    dir_path = RunAllCase().run()
    EmailUtiles().send_email()
    # EmailUtiles(dir_path).zip_send_email()