from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common import config_value
import os

current_path = os.path.dirname(__file__)
dri_path = os.path.join(current_path, config_value.config.chrome_path)


class Browser:
    def __init__(self, driver_path=dri_path, driver_name=config_value.config.driver_name):
        self.__driver_name = driver_name
        self.__driver_path = driver_path

    def get_driver(self):
        if str(self.__driver_name).lower() == 'chrome':
            return self.__get_chrome_driver()
        elif str(self.__driver_name).lower() == 'firefox':
            return self.__get_firefox_driver()

    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        chrome_driver_path = os.path.join(self.__driver_path, 'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.__driver_path, 'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        return driver


if __name__ == '__main__':
    Browser().get_driver()