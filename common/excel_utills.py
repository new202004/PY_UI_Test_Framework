# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: excel_utills.py
# @time: 2020/5/5 16:38
# @desc
import os
import xlrd
from common.config_value import config


class ExcelUtills:
    """
    判断是否是excel文件再进行处理  xls xlsx 并且 文件存在
    """
    def __init__(self, file_path, sheet_name=None):
        self.excel_path = file_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:  # 当sheet_name没带参数时，默认取第一个表格
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        return self.sheet_data.nrows

    @property
    def get_col_count(self):
        return self.sheet_data.ncols

    def get_sheet_data_by_list(self):
        all_excel_data = []
        for row in range(self.get_row_count):
            row_excel_data = []
            for col in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(row, col)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../element_info_datas/elements_info.xlsx')
    sheet_name = 'element_infos'
    excel_utills = ExcelUtills(excel_path, sheet_name)

    for i in excel_utills.get_sheet_data_by_list():
        print(i)
