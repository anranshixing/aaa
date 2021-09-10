from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if self.driver is None:
            caps = dict()
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
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator, time=20):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))
