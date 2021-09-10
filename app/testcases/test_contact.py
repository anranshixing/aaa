from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeiXing:
    def setup_class(self):
        desired_caps={
            'platformName': 'android',
            'platformVersion': '8.1.0',
            'deviceName': '2178ca60',
            # 'appPackage': 'com.tencent.wework',
            'appPackage': '__UNI__C33F03B_0831091139',
            # 'appActivity': '.launch.WwMainActivity',
            'noReset': 'true',
            'skipServerInstallation': True,
            'skipDeviceInitialization': True

        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_addcontact(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        size = self.driver.get_window_size()
        e1 = (MobileBy.XPATH,'//*[@text="添加客户"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(e1))
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
