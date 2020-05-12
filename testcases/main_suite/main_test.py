import unittest
from actions.quit_action import QuitAction
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils
from element_infos.main import main_page


class MainTest(SeleniumBaseCase):
    test_class_info = TestDataUtils('main_suite', 'main_test').convert_exceldata_to_testdata()

    # 退出登录
    @unittest.skipIf(test_class_info['test_logout']['is_not'], '')
    def test_logout(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        quit_action = QuitAction(self.base_page.driver)
        login_page = quit_action.quit_action()
        actual_result = login_page.get_title()

        test_function_data = self.test_class_info['test_logout']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 获取公司名称
    @unittest.skipIf(test_class_info['test_my_company_name']['is_not'], '')
    def test_my_company_name(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        actual_result = main_page.MainPage(self.base_page.driver).get_company_name()

        test_function_data = self.test_class_info['test_my_company_name']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 点击我的地盘
    @unittest.skipIf(test_class_info['test_click_my_zone']['is_not'], '')
    def test_click_my_zone(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_page.MainPage(self.base_page.driver).goto_myzone()
        actual_result = main_page.MainPage(self.base_page.driver).get_scedule_name()

        test_function_data = self.test_class_info['test_click_my_zone']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 点击项目
    @unittest.skipIf(test_class_info['test_click_project']['is_not'], '')
    def test_click_project(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_page.MainPage(self.base_page.driver).goto_product()

        actual_result = main_page.MainPage(self.base_page.driver).get_story_name()

        test_function_data = self.test_class_info['test_click_project']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 点击迭代
    @unittest.skipIf(test_class_info['test_click_Iterate']['is_not'], '')
    def test_click_Iterate(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_page.MainPage(self.base_page.driver).goto_iterate()

        actual_result = main_page.MainPage(self.base_page.driver).get_burndown_chart()

        test_function_data = self.test_class_info['test_click_Iterate']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 点击测试
    @unittest.skipIf(test_class_info['test_click_test']['is_not'], '')
    def test_click_test(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_page.MainPage(self.base_page.driver).goto_test_menu()

        actual_result = main_page.MainPage(self.base_page.driver).get_test_list()

        test_function_data = self.test_class_info['test_click_test']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 点击运维
    @unittest.skipIf(test_class_info['test_click_ops']['is_not'], '')
    def test_click_ops(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_page.MainPage(self.base_page.driver).goto_ops_menu()

        actual_result = main_page.MainPage(self.base_page.driver).get_engine_room()

        test_function_data = self.test_class_info['test_click_ops']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])

    # 点击办公
    @unittest.skipIf(test_class_info['test_click_office']['is_not'], '')
    def test_click_office(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_page.MainPage(self.base_page.driver).goto_office_menu()

        actual_result = main_page.MainPage(self.base_page.driver).get_attendance()

        test_function_data = self.test_class_info['test_click_office']
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, test_function_data['fail_information'])


if __name__ == '__main__':
    unittest.main()