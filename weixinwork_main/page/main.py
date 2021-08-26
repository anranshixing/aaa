from selenium.webdriver.common.by import By
from weixinwork_main.page.add_member import AddMember
from weixinwork_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member(self):
        # self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
        self.find(By.CSS_SELECTOR, '.frame_nav:nth-child(1)>a:nth-child(2)>span').click()
        self.wait_for_click((By.CSS_SELECTOR, '.ww_operationBar>a:nth-child(2)'))
        self.find(By.CSS_SELECTOR, '.ww_operationBar>a:nth-child(2)').click()
        return AddMember(self._driver)
