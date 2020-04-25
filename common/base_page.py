from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.log_utills import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 浏览器操作封装  -->  二次封装
    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址：%s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')

    def get_title(self, title):
        value = self.driver.title.text
        logger.info('获取元素名称:%s' % value)

    '''self.username_input_box = {'element_name': '用户名输入框','locator_type': 'XPATH',
    'locator_value': '//input[@name="account"]','timeout': 3}'''
    def find_element(self, element_info):
        locator_element_name = element_info['element_name']
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']

        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'id':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'XPATH':
            locator_type = By.XPATH

        logger.info('%s：  元素识别成功' % locator_element_name)
        elment = WebDriverWait(self.driver, locator_timeout)\
            .until(lambda x: x.find_element(locator_type, locator_value_info))

        return elment

        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')))

    # 点击
    def click(self, element_info):
        self.find_element(element_info).click()
        logger.info('%s：  点击操作成功' % element_info['element_name'])

    # 输入内容
    def input(self, element_info, content):
        self.find_element(element_info).send_keys(content)
        logger.info('%s：  输入内容【%s】' % (element_info['element_name'], content))

    # 获取属性值
    def get_attribute(self, element_info):
        value = self.find_element(element_info).get_attribute('title')
        logger.info('%s：  属性值为【%s】' % (element_info['element_name'], value))

    # 获取文本信息
    def get_text(self, element_info):
        text = self.find_element(element_info).text
        logger.info('%s：  对象的文本信息为【%s】' % (element_info['element_name'], text))

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()









