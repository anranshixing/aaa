from selenium.webdriver.remote import webdriver

from test_qbjh.page.base_page import BasePage
from test_qbjh.page.login import Login


class Main(BasePage):



    def goto_login(self):
        pass
        return Login(self._driver)
