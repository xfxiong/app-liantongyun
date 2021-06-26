from appium.webdriver.common.mobileby import MobileBy

agree_btn = MobileBy.ID, "com.hcloud.wocom:id/tv_right"
pwd_login_link = MobileBy.ID, "com.hcloud.wocom:id/tv_psw"
phone_num_input = MobileBy.ID, "com.hcloud.wocom:id/et_phone"
pwd_input = MobileBy.ID, "com.hcloud.wocom:id/et_psw"
login_next_btn = MobileBy.ID, "com.hcloud.wocom:id/bt_next"

error_txt = MobileBy.ID, "com.hcloud.wocom:id/tv_error"

my_btn = MobileBy.XPATH, "//*[contains(@text,'我的')]"

setting_btn = MobileBy.ID, "com.hcloud.wocom:id/iv_setting"

logout_btn = MobileBy.ID, "com.hcloud.wocom:id/bt_out_login"
logout_confirm_btn = MobileBy.ID, "com.hcloud.wocom:id/tv_right"
