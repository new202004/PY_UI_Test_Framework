from common.base_page import BasePage
from common import login
from common.config_value import config
from common import set_driver


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input_box = {'element_name': '用户名输入框',
                                   'locator_type': 'XPATH',
                                   'locator_value': '//input[@name="account"]',
                                   'timeout': 3}

        self.password_input_box = {'element_name': '密码输入框',
                                   'locator_type': 'XPATH',
                                   'locator_value': '//input[@name="password"]',
                                   'timeout': 3}

        self.login_button = {'element_name': '登录按钮',
                             'locator_type': 'XPATH',
                             'locator_value': '//button[@id="submit"]',
                             'timeout': 3}

    def input_username(self, username):  # 方法 == 》 控件的操作
        self.input(self.username_input_box, username)

    def input_password(self, password):
        self.input(self.password_input_box, password)

    def click_login(self):
        self.click(self.login_button)


if __name__ == '__main__':
    driver = set_driver.set_driver()
    # 测试用例一：登录成功
    login.test_login(config.zantao_url, config.user_name, config.password, driver)
    # 测试用例二：登录失败
    driver = set_driver.set_driver()
    login.test_login(config.zantao_url, config.user_name, (config.password + '1'), driver)
