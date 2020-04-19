from common import login
from common.config_value import config
from common import set_driver
from common.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.company_show_box = {'element_name': '公司名称',
                                 'locator_type': 'XPATH',
                                 'locator_value': '//h1[@id="companyname"]',
                                 'timeout': 3}
        self.my_zone_menu = {'element_name': '我的地盘',
                             'locator_type': 'XPATH',
                             'locator_value': '//li[@data-id="my"]',
                             'timeout': 3}
        self.product_menu = {'element_name': '项目',
                             'locator_type': 'XPATH',
                             'locator_value': '//li[@data-id="product"]',
                             'timeout': 3}
        self.username_show_span = {'element_name': '用户名称',
                                   'locator_type': 'XPATH',
                                   'locator_value': '//span[@class="user-name"]',
                                   'timeout': 3}
        self.logout_menu = {'element_name': '签退',
                            'locator_type': 'XPATH',
                            'locator_value': '//a[@id="signOut"]',
                            'timeout': 3}
        self.zentao_vaesion = {'element_name': '禅道版本',
                               'locator_type': 'XPATH',
                               'locator_value': '//a[@href="https://www.zentao.net"]',
                               'timeout': 3}
        self.forget_password_menu = {'element_name': '忘记密码',
                                     'locator_type': 'XPATH',
                                     'locator_value': '//a[@href="/biz/my-changepassword.html?onlybody=yes"]',
                                     'timeout': 3}
        self.forget_password_original_password = {'element_name': '修改密码——原密码',
                                                  'locator_type': 'XPATH',
                                                  'locator_value': '//input[@id="originalPassword"]',
                                                  'timeout': 3}
        self.forget_password_password1 = {'element_name': '修改密码——新密码',
                                          'locator_type': 'XPATH',
                                          'locator_value': '//input[@id="password1"]',
                                          'timeout': 3}
        self.forget_password_password2 = {'element_name': '修改密码——重复新密码',
                                          'locator_type': 'XPATH',
                                          'locator_value': '//input[@id="password2"]',
                                          'timeout': 3}
        self.forget_password_save_button = {'element_name': '修改密码——保存按钮',
                                            'locator_type': 'XPATH',
                                            'locator_value': '//button[@id="submit"]',
                                            'timeout': 3}

    def get_company_name(self):
        value = self.get_attribute(self.company_show_box)
        return value

    def goto_myzone(self):
        self.click(self.my_zone_menu)

    def goto_product(self):
        self.click(self.product_menu)

    def get_user_name(self):
        text = self.get_text(self.username_show_span)
        return text

    def get_zentao_version(self):
        zantao_version = self.get_text(self.zentao_vaesion)
        return zantao_version

    def goto_forget_password(self):
        self.click(self.username_show_span)
        self.click(self.forget_password_menu)

    def change_password(self, original_password, password1, password2):
        self.driver.switch_to.frame('iframe-triggerModal')
        self.input(self.forget_password_original_password, original_password)
        self.input(self.forget_password_password1, password1)
        self.input(self.forget_password_password2, password2)
        self.click(self.forget_password_save_button)
        self.driver.switch_to.default_content()

    def logout(self):
        self.click(self.logout_menu)


if __name__ == '__main__':
    driver = set_driver.set_driver()
    login.test_login(config.zantao_url, config.user_name, config.password, driver)
    main_page = MainPage(driver)
    # 测试用例三：获取"我的公司"名称
    company_name = main_page.get_company_name()
    # 测试用例四：点击【我的地盘】
    main_page.goto_myzone()
    # 测试用例五：点击【项目】
    main_page.goto_product()
    # 测试用例六：获取用户名称文本信息
    username_text = main_page.get_user_name()
    # 测试用例七：获取禅道版本
    zantao_version = main_page.get_zentao_version()
    # 测试用例八：点击忘记密码
    main_page.goto_forget_password()
    # 测试用例九：修改密码
    main_page.change_password(config.password, config.password, config.password)
    # 测试用例十： 签退
    main_page.logout()
