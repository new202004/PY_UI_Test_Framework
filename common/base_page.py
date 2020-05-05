import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from common.log_utills import logger
from common.config_value import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 浏览器操作封装  -->  二次封装
    def open_url(self, url):
        try:
            self.driver.get(url)
            logger.info('打开url地址：%s' % url)
        except Exception as e:
            logger.error('不能打开指定的特殊网址，原因是：%s' % e.__str__())

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')

    def close_tab(self):
        self.driver.close()
        logger.info('关闭当前页面')

    def exit_driver(self):
        self.driver.quit()
        logger.info('退出浏览器')

    def get_title(self):
        value = self.driver.title
        logger.info('获取元素名称:%s' % value)
        return value

    '''self.username_input_box = {'element_name': '用户名输入框','locator_type': 'XPATH',
    'locator_value': '//input[@name="account"]','timeout': 3}'''
    def find_element(self, element_info):
        """
        根据提供的元素参数信息进行查找
        :param element_info: 元素信息，字典类型
        :return: element对象
        """
        try:
            locator_element_name = element_info['element_name']
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']

            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'class_name':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'XPATH':
                locator_type = By.XPATH

            elment = WebDriverWait(self.driver, int(locator_timeout))\
                .until(lambda x: x.find_element(locator_type, locator_value_info))
            logger.info('%s：  元素识别成功' % locator_element_name)
        except Exception as  e:
            logger.error('%s：  元素识别失败，原因是：%s' % (locator_element_name, e.__str__()))
            self.screenshot_as_file()
        # finally:
        #     if elment is None:
        #         elment = ''
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
        return text

    # franme处理
    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)
        time.sleep(1)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        time.sleep(1)

        # 包含：frame处理、windows句柄处理、alert处理、鼠标常用操作、键盘常用操作）

    # windows句柄处理
    # 1. 获取当前句柄
    def get_handle_window(self):
        return self.driver.current_window_handle

    # 2. 跳转指定句柄
    def switch_to_window(self, window_handle):
        return self.driver.switch_to.window(window_handle)

    # 2.切换到指定句柄
    def switch_window_by_title(self, title):
        for handle in self.driver.window_handles:
            if WebDriverWait(driver, config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(handle)
                if self.driver.title.__contains__(title):
                    break
        time.sleep(1)

    def switch_window_by_url(self, url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url.__contains__(url):
                break
        time.sleep(1)

    # alert处理
    # 1.alert 弹窗
    def alert(self, content):
        alert_str = 'alert("%s")' % content
        self.driver.execute_script(alert_str)

    # 2.切换到js弹窗，获取弹窗提示值，点击确定
    def switch_to_alert(self, action='accept', timeout=int(config.time_out)):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        if action == 'accept':
            logger.info('弹窗提示值为：  %s' % text)
            alert.accept()
        else:
            alert.dismiss()
        return text

    # 鼠标键盘封装（建议代码思路：判断操作系统类型）
    # 1.鼠标右击
    def mouse_right_click(self, element_info):
        mouse = ActionChains(self.driver)
        element = self.find_element(element_info)
        mouse.context_click(element).perform()

    # 2. 鼠标长按
    def mouse_click_and_hold(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(10).release(element).perform()

    # 3. 鼠标移动到某个元素
    def mouse_move_to_element(self, element_info):
        element = self.find_element(element_info)
        mouse = ActionChains(self.driver)
        mouse.move_to_element(element).perform()

    # 键盘常用操作
    def key_board_operate(self, element, operate):
        # element = self.find_element(element_info)
        if operate == 'tab':
            element.send_keys(Keys.TAB)   # 1.按下tab键
        elif operate == 'back_space':      # 2.回退
            element.send_keys(Keys.BACK_SPACE)
        elif operate == 'ctrl c':
            element.send_keys(Keys.CONTROL, 'c')  # 复制
        elif operate == 'ctrl v':
            element.send_keys(Keys.CONTROL, 'v')  # 粘贴

    # 封装固定等待
    def wait(self, seconds=config.time_out):
        time.sleep(seconds)

    # 封装显式等待
    def time(self, seconds=config.time_out):
        self.driver.implicitly_wait(seconds)

    # 截图封装
    def screenshot_as_file(self, *screenshot_path):
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path) == 0:
            screenshot_file_path = config.screen_shot_path
        else:
            screenshot_file_path = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_file_path = os.path.join(current_dir, screenshot_file_path, 'UI_test_%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_file_path)


if __name__ == '__main__':
    from common.browser import browser
    driver = browser.get_driver()
# # 调试windows句柄
#     driver.get('http://jtj.kaifeng.gov.cn/')
#     driver.maximize_window()
#     driver.find_element(By.XPATH, '//a[@href="http://kf.hnzwfw.gov.cn/hnzw/bmft/index/bm_index.do?webId=3&deptid='
#                                   '001003012002024"]').click()
#     # BasePage(driver).switch_window_by_url('http://jtj.kaifeng.gov.cn/')
#     BasePage(driver).switch_window_by_title('开封市教育体育网')
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//a[@href="/xxfc/"]').click()
#     # driver.close()

# # 调试alert
#     js_str = "hello"
#     BasePage(driver).alert(js_str)
#     time.sleep(2)
#     BasePage(driver).switch_to_alert()
#
# # 调试鼠标常用操作
#     driver.get('https://www.baidu.com/')
#     # locator_value_info = '//input[@type="submit"]'
#     locator_value_info = '//a[@href="http://www.baidu.com/gaoji/preferences.html"]'
#     elment = WebDriverWait(driver, int(5))\
#             .until(lambda x: x.find_element(By.XPATH, locator_value_info))
#
#     # BasePage(driver).mouse_right_click(elment)
#     BasePage(driver).mouse_click_and_hold(elment)

# 调试键盘操作
    driver.get('https://www.baidu.com/')
    locator_value_info = '//input[@id="kw"]'
    elment = WebDriverWait(driver, int(5))\
            .until(lambda x: x.find_element(By.XPATH, locator_value_info))
    # elment.send_keys('111')
    BasePage(driver).key_board_operate(elment, 'ctrl v')

