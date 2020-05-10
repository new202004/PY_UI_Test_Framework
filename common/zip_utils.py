# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: zip_utils.py
# @time: 2020/5/10 10:15
# @desc
import os
import zipfile


def zip_dir(dir_path, zip_path):
    '''
    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    '''
    zip = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        print(root)
        print(dir_path)
        file_path = root.replace(dir_path, '')  # 去掉根路径，只对文件夹下的文件及文件夹进行压缩
        # 循环出一个个文件名
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
        zip.close()


if __name__ == '__main__':
    # current_path = os.path.dirname(__file__)
    # report_path = os.path.join(current_path, '../reports/禅道自动化测试报告-PYV1.5')
    # dir_path = os.path.join(current_path, report_path)
    # zip_report_path = os.path.join(current_path, '../reports')
    # zip_path = os.path.join(current_path, zip_report_path)
    zip_dir(r"G:\python_code\PY_UI_Test_Framework_class\reports\禅道自动化测试报告-PYV1.5", r"G:\python_code\PY_UI_Test_Framework_class\reports" + '.zip')


