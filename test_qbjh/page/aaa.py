from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:


    def __init__(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['platformVersion'] = '8.1'
        caps['deviceName'] = '2178ca60'
        caps['appPackage'] = 'com.cherish.app.view'
        # caps['appPackage'] = 'com.tencent.mm'
        # caps['appActivity'] = '.ui.LauncherUI'
        caps['appActivity'] = 'io.dcloud.PandoraEntryActivity'
        caps['noReset'] = True
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)
        size = self.driver.get_window_size()
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,'//*[@text="微信"]')))
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.1, size['width'] * 0.5, size['height'] * 0.9)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="柒芮斯"]').click()
        sleep(2)
        print(self.driver.contexts)

        # self.driver.switch_to.context(contexts[1])


    def goto_login(self):
        print(self.driver.contexts)
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, '我的')))
        self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="我的"])[2]').click()
