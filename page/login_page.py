import time

import page
from bases.base import Base


class LoginPage(Base):
    def agree(self):
        # 点击同意
        self.click(page.agree_btn)

    def login(self, username, pwd):
        # 点击密码登录
        self.click(page.pwd_login_link)
        # 输入账号
        self.input(page.phone_num_input, username)
        # 输入密码
        self.input(page.pwd_input, pwd)
        # 点击登录
        self.click(page.login_next_btn)

    def goto_my(self):
        # 点击我的
        self.click(page.my_btn)

    def goto_setting(self):
        # 点击设置
        self.click(page.setting_btn)

    def logout(self):
        # 点击退出登录
        self.click(page.logout_btn)
        # 点击确定
        self.click(page.logout_confirm_btn)

    # 获取登录错误提示文本/toast
    def get_error_text(self, toast):
        if self.element_is_exist(page.error_txt):
            return self.find_element(page.error_txt).text
        else:
            return self.driver.find_element_by_xpath(f"// *[contains(@text,'{toast}')]").text

    def screenshot(self):
        self.driver.get_screenshot_as_file("/image/{}".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    def login_if_success(self):
        return self.element_is_exist(page.my_btn)

    def logout_if_success(self):
        return self.element_is_exist(page.pwd_login_link)
