from common import login
from common.config_value import config
from common.browser import browser
from common.base_page import BasePage
# from common.element_yaml_utills import ElementYamlData
from common.element_data_utills import get_page_info

elements = get_page_info('main',  'main')
# elements = ElementYamlData('main_page').read_yaml()


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.company_show_box = elements['company_show_box']
        self.my_zone_menu = elements['my_zone_menu']
        self.product_menu = elements['product_menu']
        self.username_show_span = elements['username_show_span']
        self.logout_menu = elements['logout_menu']
        self.zentao_vaesion = elements['zentao_vaesion']
        self.forget_password_menu = elements['forget_password_menu']
        self.forget_password_original_password = elements['forget_password_original_password']
        self.forget_password_password1 = elements['forget_password_password1']
        self.forget_password_password2 = elements['forget_password_password2']
        self.forget_password_save_button = elements['forget_password_save_button']
        self.story_name = elements['story_name']

        self.scedule_name = elements['scedule_name']
        self.iterate_menu = elements['iterate_menu']
        self.burndown_chart = elements['burndown_chart']

        self.test_menu = elements['test_menu']
        self.test_list = elements['test_list']
        self.ops_menu = elements['ops_menu']
        self.engine_room = elements['engine_room']
        self.office_menu = elements['office_menu']
        self.attendance = elements['attendance']

    def get_company_name(self):
        value = self.get_attribute(self.company_show_box)
        return value

    def get_scedule_name(self):
        value = self.get_text(self.scedule_name)
        return value

    def get_test_list(self):
        value = self.get_text(self.test_list)
        return value
    def get_engine_room(self):
        value = self.get_text(self.engine_room)
        return value
    def get_attendance(self):
        value = self.get_text(self.attendance)
        return value

    def get_story_name(self):
        value = self.get_text(self.story_name)
        return value

    def get_burndown_chart(self):
        value = self.get_text(self.burndown_chart)
        return value

    def goto_myzone(self):
        self.click(self.my_zone_menu)

    def goto_test_menu(self):
        self.click(self.test_menu)

    def goto_ops_menu(self):
        self.click(self.ops_menu)

    def goto_office_menu(self):
        self.click(self.office_menu)

    def goto_product(self):
        self.click(self.product_menu)

    def goto_iterate(self):
        self.click(self.iterate_menu)

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
        self.switch_to_frame('iframe-triggerModal')
        self.input(self.forget_password_original_password, original_password)
        self.input(self.forget_password_password1, password1)
        self.input(self.forget_password_password2, password2)
        self.click(self.forget_password_save_button)
        self.switch_to_default_content()

    def logout(self):
        self.click(self.username_show_span)
        self.click(self.logout_menu)


if __name__ == '__main__':
    driver = browser.get_driver()
    driver.get(config.zantao_url)
    login.test_login(config.zantao_url, config.user_name, config.password, driver)
    main_page = MainPage(driver)
    # # 测试用例三：获取"我的公司"名称
    # company_name = main_page.get_company_name()
    # # 测试用例四：点击【我的地盘】
    # main_page.goto_myzone()
    # # 测试用例五：点击【项目】
    # main_page.goto_product()
    # # 测试用例六：获取用户名称文本信息
    # username_text = main_page.get_user_name()
    # # 测试用例七：获取禅道版本
    # zantao_version = main_page.get_zentao_version()
    # # 测试用例八：点击忘记密码
    # main_page.goto_forget_password()
    # # 测试用例九：修改密码
    # main_page.change_password(config.password, config.password, config.password)
    # 测试用例十： 签退
    # main_page.logout()

    main_page.goto_product()
    scedule_name = main_page.get_story_name()

    driver.close()
