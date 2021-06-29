import allure
import pytest
from bases.app import App
from bases.logger import GetLogger
from page.login_page import LoginPage
from tools.read_yaml import get_login_data

log = GetLogger().get_logger()


class Test_Login():
    driver = None

    def setup_class(self):
        try:
            self.driver = App.start_app()
            self.login = LoginPage(self.driver)
            self.login.agree()
        except Exception as e:
            log.error(e)

    def teardown_class(self):
        App.close_app()

    @allure.feature("功能模块")
    @allure.story("密码登录页面")
    @allure.title("登录页面-{title}")
    # @allure.description("密码登录，输入账号，输入密码，点击登录")
    @allure.step("1.点击密码登录  2.输入账号，输入密码，点击登录")
    @pytest.mark.parametrize("username,pwd,expect,success,title", get_login_data())
    def test_login(self, username, pwd, success, expect, title):
        '''
        用例描述：
        前提：已有账号
        步骤：1.点击密码登录  2.输入账号，输入密码，点击登录
        '''
        self.login.login(username, pwd)
        if success:
            try:
                assert self.login.login_if_success()
            except Exception as e:
                log.error(e)
                self.login.screenshot()
            with allure.step("退出登录：点击我的，点击设置，点击退出登录"):
                self.login.goto_my()
                self.login.goto_setting()
                self.login.logout()
            try:
                assert self.login.logout_if_success()
            except Exception as e:
                log.error(e)
                self.login.screenshot()
        else:
            try:
                message = self.login.get_error_text(expect)
                print(message)
                assert message == expect
            except Exception as e:
                log.error(e)
                self.login.screenshot()
