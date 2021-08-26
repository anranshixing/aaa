import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from weixinwork_main.page.base_page import BasePage


class AddMember(BasePage):


    def add_member(self):
        self.find(By.ID, 'username').send_keys(f'hjhd{random.randint(1,99)}q')
        self.find(By.ID, 'memberAdd_acctid').send_keys(f'weqw{random.randint(1,9)}dq3{random.randint(1,9)}')
        self.find(By.ID, 'memberAdd_phone').send_keys(f'131{random.randint(1,9)}329754{random.randint(1,9)}')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # self._driver.quit()
        return True
    def get_member(self):
        self.wait_for_click((By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)'))
        members = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [member.get_attribute('title') for member in members]
