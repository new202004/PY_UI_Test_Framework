import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import log_utills
from common.base_page import BasePage


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


        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        # self.username_input_box = self.driver.find_element(By.XPATH, '//input[@name="account"]')  # 属性  ==》 页面上的控件
        # self.password_input_box = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        # self.login_button = self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        # self.keep_login_check_box = self.driver.find_element(By.XPATH, '//input[@id="keepLoginon"]')

    # def input_username(self, username):  # 方法 == 》 控件的操作
    #     self.driver.find_element()
    #     self.username_input_box.send_keys(username)
    #     self.logger.info('登录用户名为:%s' % username)
    #
    # def input_password(self, password):
    #     self.password_input_box.send_keys(password)
    #     self.logger.info('登录密码为:%s' % password)
    #
    # def click_login(self):
    #     self.login_button.click()


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver')
    logger = log_utills.logger
    driver = webdriver.Chrome(executable_path=driver_path)
    login = LoginPage(driver)
    login.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login.input_username('test01')
    login.input_password('newdream123')
    login.click_login()
