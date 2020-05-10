import unittest
from actions.quit_action import QuitAction
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase


class QuitTest(SeleniumBaseCase):
    def test_logout(self):
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        quit_action = QuitAction(self.base_page.driver)
        login_page = quit_action.quit_action()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'), True, '测试用例-退出禅道：不通过')


if __name__ == '__main__':
    unittest.main()