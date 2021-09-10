from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestXueQiu:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['skipDeviceInitialization'] = True
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)
        # WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable((MobileBy.ID,'com.yiban.app:id/btn_use')))
        # self.driver.find_element(MobileBy.ID,'com.yiban.app:id/btn_use').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("知道了")').click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("允许")').click()
    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print(self.driver.contexts)
        e1 = self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']")
        e2 = self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"基金开户")
        # e1 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search")
        e1.click()
        e2.click()
        print(self.driver.page_source)
        print(self.driver.contexts)
        # e2=self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        # e2.send_keys('alibaba')
        # sleep(3)
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el2.send_keys("alibabba")
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/name")
        # el3.click()
        # el4 = self.driver.find_element_by_id("com.xueqiu.android:id/action_delete_text")
        # el4.click()
        # el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.TextView")
        # el5.click()