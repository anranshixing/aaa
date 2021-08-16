import shelve
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test_demo1():
    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_selenium(self):
        # self.driver.find_element(By.ID,'su').click()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open('cookie')
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiy" in cookie:
                cookie.pop("expiy")
            self.driver.add_cookie(cookie)
        db.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(8)


