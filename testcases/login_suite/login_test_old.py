import unittest
from actions.login_action import LoginAction
from common.browser import browser
from common.base_page import BasePage
from common.config_value import config


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser.get_driver()
        self.base_page = BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.time()
        self.base_page.open_url(config.zantao_url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

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
