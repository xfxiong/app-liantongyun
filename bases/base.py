from selenium.webdriver.support.wait import WebDriverWait

from bases.logger import GetLogger

log = GetLogger().get_logger()


class Base():
    def __init__(self, driver):
        log.info("初始化driver{}".format(driver))
        self.driver = driver

    def find_element(self, loc, timeout=30, p=0.5):
        log.info("查找元素{}".format(loc))
        return self.driver.find_element(*loc)
        # return WebDriverWait(self.driver,timeout=timeout,poll_frequency=p).until(lambda x:x.find_element(*loc))

    def click(self, loc):
        log.info("点击元素{}".format(loc))
        self.find_element(loc).click()

    def input(self, loc, value):
        log.info("给元素{}输入{}".format(loc, value))
        el = self.find_element(loc)
        log.info("清空元素{}".format(loc))
        el.clear()
        log.info("给元素输入内容{}".format(value))
        el.send_keys(value)

    def scroll(self):
        pass

    # def send_keys(self,loc,value):
    #     self.find_element(loc).send_keys(value)
    # def clear(self,loc):
    #     self.find_element(loc).clear()

    def get_text(self, loc):
        log.info("获取元素{}的文本信息".format(loc))
        return self.find_element(loc).text

    def element_is_exist(self, loc):
        try:
            log.info(f"查找元素{loc}是否存在")
            self.find_element(loc)
            return True
        except:
            return False
