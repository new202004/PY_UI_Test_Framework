import os
import configparser


class ConfigValue:
    def __init__(self):
        self.current_path = os.path.dirname(__file__)
        self.conf_path = os.path.join(self.current_path, '../conf/local_config.ini')
        self.conf = configparser.ConfigParser()
        self.conf_data = self.conf.read(self.conf_path, encoding='utf-8')

    @property
    def zantao_url(self):
        return self.conf.get("zentao", "zentao_url")

    @property
    def user_name(self):
        return self.conf.get("user", "user_name")

    @property
    def password(self):
        return self.conf.get("user", "password")

    @property
    def chrome_path(self):
        return self.conf.get("driver", "chrome_path")

    @property
    def driver_name(self):
        return self.conf.get("driver", "driver_name")

    @property
    def time_out(self):
        return self.conf.get("time", "time_out")

    @property
    def screen_shot_path(self):
        return self.conf.get("default", "screen_shot_path")

    @property
    def test_data_path(self):
        return self.conf.get("default", "test_data_path")

    @property
    def case_path(self):
        return self.conf.get("default", "case_path")

    @property
    def report_path(self):
        return self.conf.get("default", "report_path")


config = ConfigValue()

if __name__ == '__main__':
    zantao_url = config.zantao_url
    user_name = config.user_name
    password = config.password
    chrome_path = config.chrome_path
    driver_name = config.driver_name
    time_out = config.time_out
    test_data_path = config.test_data_path
    case_path = config.case_path
    report_path = config.report_path

    print(report_path, case_path, test_data_path, zantao_url, user_name, password, chrome_path, driver_name, time_out)
