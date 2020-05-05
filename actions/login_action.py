from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.browser import browser
from common.config_value import config


class LoginAction:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)

    def login_action(self, username, password, url=config.zantao_url):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    # 登录成功
    def login_success(self, username, password):
        self.login_action(username, password)
        return MainPage(self.login_page.driver)

    # 登录失败
    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.switch_to_alert()

    # 默认登录
    def default_login(self):
        self.login_success(config.user_name, config.password)

    # 通过cookie登录
    def login_by_cookie(self):
        pass


if __name__ == '__main__':
    driver = browser.get_driver()
    login_action = LoginAction(driver)
    # login_action.login_success(config.user_name, config.password)
    # login_action.close_driver()
    driver.get(config.zantao_url)
    alert_content = login_action.login_fail(config.user_name, (config.password + '1'))
    print(alert_content)
