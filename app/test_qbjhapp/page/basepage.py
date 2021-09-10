from appium import webdriver
class BasePage:

    def setup_method(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['platformVersion'] = '8.1'
        caps['deviceName'] = '2178ca60'
        caps['appPackage'] = 'com.cherish.app.view'
        caps['appActivity'] = 'io.dcloud.PandoraEntryActivity'
        caps['noReset'] = True
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def