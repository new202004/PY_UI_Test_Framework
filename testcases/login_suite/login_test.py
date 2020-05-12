import unittest
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    test_class_info = TestDataUtils('login_suite', 'login_test').convert_exceldata_to_testdata()

    def setUp(self) -> None:
        super().setUp()
        self.base_page.wait(1)
        self.base_page.refresh()

    def tearDown(self) -> None:
        pass

    @unittest.skipIf(test_class_info['test_login_success']['is_not'], '')
    def test_login_success(self):
        test_function_data = self.test_class_info['test_login_success']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('user_name'),
                                               test_function_data['test_parameter'].get('password'))
        self.assertEqual(main_page.get_user_name(), (test_function_data['excepted_result']), test_function_data['fail_information'])

    @unittest.skipIf(test_class_info['test_login_fail']['is_not'], '')
    def test_login_fail(self):
        test_function_data = self.test_class_info['test_login_fail']
        login_action = LoginAction(self.base_page.driver)
        alert_content = login_action.login_fail(test_function_data['test_parameter'].get('user_name'),
                                               test_function_data['test_parameter'].get('password'))
        alert_actual_content = test_function_data['excepted_result']
        self.assertEqual(alert_content, alert_actual_content, test_function_data['fail_information'])


if __name__ == '__main__':
    unittest.main()
