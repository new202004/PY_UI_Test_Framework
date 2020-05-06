import os
import xlrd
from common.config_value import config
from common.excel_utills import ExcelUtills

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/elements_info.xlsx')


class ElementDataUtills:
    def __init__(self, module_name, element_path=excel_path):
        self.excel_data = ExcelUtills(element_path, module_name).get_sheet_data_by_list()

    def get_element_info(self, page_name):
        element_infos = {}
        for page_data in self.excel_data:
            if page_data[0] == page_name:
                element_info = {'element_name': page_data[2],
                                'locator_type': page_data[3],
                                'locator_value': page_data[4], 'timeout':
                                    int(page_data[5]) if isinstance(page_data[5], float) else config.time_out}
                element_infos[page_data[1]] = element_info
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
