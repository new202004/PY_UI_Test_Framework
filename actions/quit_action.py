from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.browser import browser
from common.config_value import config


class QuitAction:
    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def quit_action(self):
        self.main_page.logout()
        return LoginPage(self.main_page.driver)