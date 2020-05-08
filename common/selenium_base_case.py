import unittest
from common.base_page import BasePage
from common.browser import browser
from common.config_value import config
from common.log_utills import logger


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('==========测试类开始执行==========')

        cls.url = config.zantao_url

    def setUp(self) -> None:
        logger.info('----------测试方法开始执行----------')
        self.driver = browser.get_driver()
        self.base_page = BasePage(self.driver)
        self.base_page.set_browser_max()
        self.base_page.time()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        # 测试失败用例截图
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                self.base_page.screeshot_as_file()

        self.base_page.close_tab()
        logger.info('----------测试方法开始完毕----------')

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('==========测试类执行完毕==========')
        pass

