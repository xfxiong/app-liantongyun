import yaml
from appium import webdriver

with open("../datas/caps.yaml") as f:
    myconfig = yaml.safe_load(f)
    desired_caps = myconfig['desirecaps']


class App:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def start_app(cls):
        if cls.driver == None:
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def close_app(cls):
        if cls.driver:
            cls.driver.quit()
        cls.driver = None

    def restart(self):
        pass

    def stop(self):
        pass
