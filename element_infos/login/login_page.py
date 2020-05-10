from common.base_page import BasePage
from common.config_value import config
from common.browser import browser
# from common.element_yaml_utills import ElementYamlData
from common.element_data_utills import get_page_info

elements = get_page_info('login', 'login')
# elements = ElementYamlData('login_page').read_yaml()


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input_box = elements['username_input_box']
        self.password_input_box = elements['password_input_box']
        self.login_button = elements['login_button']

    def input_username(self, username):  # 方法 == 》 控件的操作
        self.input(self.username_input_box, username)

    def input_password(self, password):
        self.input(self.password_input_box, password)

    def click_login(self):
        self.click(self.login_button)

    def get_login_fail_alert(self):
        return self.switch_to_alert()


if __name__ == '__main__':
    driver = browser.get_driver()
    driver.get(config.zantao_url)
    # # 测试用例一：登录成功
    # login.test_login(config.zantao_url, config.user_name, config.password, driver)
    # driver.close()
    # # 测试用例二：登录失败
    # driver = browser.get_driver()
    # login.test_login(config.zantao_url, config.user_name, (config.password + '1'), driver)
    # driver.close()

    BasePage(driver).screenshot_as_file()