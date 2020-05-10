import os
from common.config_value import config
from common.excel_utills import ExcelUtills

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, config.element_info_path)


class ElementDataUtills:
    def __init__(self, module_name, page_name, element_path=excel_path):
        page_excel_path = os.path.join(element_path, module_name, page_name + '.xlsx')
        self.excel_data = ExcelUtills(page_excel_path).get_sheet_data_by_list()

    def get_element_info(self):
        element_infos = {}
        for page_data in self.excel_data:
            element_info = {'element_name': page_data[1],
                            'locator_type': page_data[2],
                            'locator_value': page_data[3], 'timeout':
                                int(page_data[3]) if isinstance(page_data[3], float) else config.time_out}
            element_infos[page_data[0]] = element_info
        return element_infos


def get_page_info(module_name, page_name):
    element_data = ElementDataUtills(module_name, page_name)
    elements = element_data.get_element_info()
    return elements


if __name__ == '__main__':
    module = 'login'
    page = 'login'
    elements = get_page_info(module, page)
    for e in elements.values():
        print(e)
