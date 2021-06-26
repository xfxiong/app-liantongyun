import allure
import pytest
from bases.app import App
from bases.logger import GetLogger
from page.login_page import LoginPage

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

    @allure.story("密码登录")
    @pytest.mark.parametrize("username,pwd,success,expect",
                             [("18000000001", "Abc1234@", True, "登录成功"), ("", "Abc1234@", False, "请输入正确的11位手机号"),
                              ("18000000001", "", False, "请输入登录密码")])
    def test_login(self, username, pwd, success, expect):
        self.login.login(username, pwd)
        if success:
            try:
                assert self.login.login_if_success()
            except Exception as e:
                log.error(e)
                self.login.screenshot()
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
