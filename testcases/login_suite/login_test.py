import unittest
from actions.login_action import LoginAction
from common.config_value import config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.base_page.wait(3)
        self.base_page.refresh()
        self.test_class_info = TestDataUtils('login_suite').convert_exceldata_to_testdata('LoginTest')

    def tearDown(self) -> None:
        pass

    def test_login_success(self):
        test_function_data = self.test_class_info['test_login_success']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('user_name'),
                                               test_function_data['test_parameter'].get('password'))
        self.assertEqual(main_page.get_user_name(), test_function_data['excepted_result'], '测试用例-登录成功：执行失败')

    def test_login_fail(self):
        test_function_data = self.test_class_info['test_login_fail']
        login_action = LoginAction(self.base_page.driver)
        alert_content = login_action.login_fail(test_function_data['test_parameter'].get('user_name'),
                                               test_function_data['test_parameter'].get('password'))
        alert_actual_content = test_function_data['excepted_result']
        self.assertEqual(alert_content, alert_actual_content, '测试用例-登录失败：执行失败')


if __name__ == '__main__':
    unittest.main()
