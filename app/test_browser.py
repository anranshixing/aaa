from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:

    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            # 'chromedriverExecutable': ''
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        self.driver.find_element(MobileBy.XPATH,'//input[@id="index-kw"]').send_keys('appuim')
        search_locator = (MobileBy.ID,'index-bn')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(search_locator))
        self.driver.find_element(*search_locator).click()