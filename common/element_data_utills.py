import os
import xlrd
from common.config_value import config

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/elements_info.xlsx')


class ElementDataUtills:
    def __init__(self, module_name, element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(self.element_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.value = self.sheet.cell_value(1, 0)
        self.row_count = self.sheet.nrows

    def get_element_info(self, page_name):
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 0) == page_name:
                element_info = {'element_name': self.sheet.cell_value(i, 2),
                                'locator_type': self.sheet.cell_value(i, 3),
                                'locator_value': self.sheet.cell_value(i, 4), 'timeout':
                                    int(self.sheet.cell_value(i, 5)) if isinstance(self.sheet.cell_value(i, 5),
                                                                                   float) else config.time_out}
                element_infos[self.sheet.cell_value(i, 1)] = element_info
        return element_infos


def get_page_info(module_name, page_name):
    element_data = ElementDataUtills(module_name)
    elements = element_data.get_element_info(page_name)
    return elements


if __name__ == '__main__':
    module = 'element_infos'
    page = 'main_page'
    elements = get_page_info(module, page)
    for e in elements.values():
        print(e)
