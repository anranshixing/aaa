from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_weixinwork_login.login import Login
from selenium_weixinwork_login.register import Register

# 首页PO
class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
    def goto_login(self):
        # click login
        self._driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)
    def goto_register(self):
        # click register
        self._driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)