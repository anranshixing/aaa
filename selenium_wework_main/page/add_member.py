from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:
    def __init__(self,driver: WebDriver):
        self._driver = driver

    def add_member(self):
        # sendkeys
        sleep(2)
        self._driver.find_element(By.ID,'username').send_keys('shixing')
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys('wqhdhldal')
        self._driver.find_element(By.ID,'memberAdd_phone').send_keys('13266666666')
        self._driver.find_element(By.XPATH,'//form/div[3]/a[2]').click()
        sleep(5)
        return True
    def get_member(self):
        members = self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        return [member.get_attribute('title') for member in members]

