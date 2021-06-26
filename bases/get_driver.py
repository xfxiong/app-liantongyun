import yaml
from appium import webdriver

with open("../datas/caps.yaml") as f:
    myconfig = yaml.safe_load(f)
    desired_caps = myconfig['desirecaps']


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # desired_caps = dict()
            # # 平台名称，大小写无所谓
            # desired_caps['platformName'] = 'Android'
            # # 平台版本（5.4.3 可以写5.4.3,5.4,5）
            # desired_caps['platformVersion'] = '7.1'
            # # 设备名称，可以随便写，但是不能乱写
            # desired_caps['deviceName'] = 'VOG-AL00'
            # # 包名
            # desired_caps['appPackage'] = 'com.hcloud.wocom'
            # # 界面名
            # desired_caps['appActivity'] = 'com.hcloud.pan.ui.activity.login.LoginNewActivity'
            # desired_caps['automationName']= "uiautomator2"
            # desired_caps["noReset"]= False  # 清空数据
            # desired_caps["unicodeKeyboard"]= True  # 使用Unicode编码方式发送字符串
            # desired_caps["resetKeyboard"]= True  # 键盘隐藏起来

            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
        cls.driver = None
