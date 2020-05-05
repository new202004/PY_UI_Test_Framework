import unittest
from actions.login_action import LoginAction
from common.config_value import config
from common.selenium_base_case import SeleniumBaseCase


class LoginTest(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.base_page.wait(3)
        self.base_page.refresh()

    def tearDown(self) -> None:
        pass

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(config.user_name, config.password)
        self.assertEqual(main_page.get_user_name(), config.user_name, '测试用例-登录成功：执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        alert_content = login_action.login_fail(config.user_name, '111111')
        alert_actual_content = '登录失败，请检查您的用户名或密码是否填写正确。'
        self.assertEqual(alert_content, alert_actual_content, '测试用例-登录失败：执行失败')


if __name__ == '__main__':
    unittest.main()
