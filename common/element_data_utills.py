import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/elements_info.xlsx')


class ElementDataUtills:
    def __init__(self, page_name, element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(self.element_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.value = self.sheet.cell_value(1, 0)
        self.row_count = self.sheet.nrows

    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.row_count):
            element_info = {'element_name': self.sheet.cell_value(i, 1), 'locator_type': self.sheet.cell_value(i, 2),
                            'locator_value': self.sheet.cell_value(i, 3), 'timeout': self.sheet.cell_value(i, 4)}
            element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos


def get_page_info(page_name):
    element_data = ElementDataUtills(page_name)
    elements = element_data.get_element_info()
    return elements


if __name__ == '__main__':
    # print(get_page_info('login_page'))
    print(__name__)