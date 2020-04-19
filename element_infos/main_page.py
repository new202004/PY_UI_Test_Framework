from selenium.webdriver.common.by import By
from element_infos import login_page
from common import log_utills
import time


class MainPage:
    def __init__(self):
        login_page.login.input_username('test01')
        login_page.login.input_password('newdream123')
        login_page.login.click_login()
        self.logger = log_utills.log

        self.driver = login_page.login.driver
        self.company_show_box = self.driver.find_element(By.XPATH, '//h1[@id="companyname"]')
        self.my_zone_menu = self.driver.find_element(By.XPATH, '//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH, '//a[@href="/zentao/www/index.php?m=product&f=index&locate=no"]')
        self.username_show_span = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')

    def get_company_name(self):
        value = self.company_show_box.get_attribute('title')
        self.logger.info('公司名称为:%s' % value)
        return value

    def goto_myzone(self):
        self.my_zone_menu.click()
        self.logger.info('点击我的地盘成功')

    def goto_product(self):
        self.product_menu.click()

    def get_user_name(self):
        value = self.username_show_span.text()
        self.logger.info('登录用户名称为:%s' % value)
        return value


if __name__ == '__main__':
    main_page = MainPage()
    company_name = main_page.get_company_name()
    main_page.goto_myzone()
    # time.sleep(3)
    # main_page.goto_product()
    username_text = main_page.get_user_name()
