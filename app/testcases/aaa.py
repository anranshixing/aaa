# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps["platformName"] = "android"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(3)

TouchAction(driver).press(x=891, y=738).move_to(x=255, y=729).release().perform()

TouchAction(driver).press(x=206, y=580).move_to(x=781, y=601).release().perform()

TouchAction(driver).tap(x=189, y=1071).perform()
driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
size = driver.get_window_size()
e1 = (MobileBy.XPATH, '//*[@text="添加客户"]')
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(e1))
driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1)
driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1)
driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

driver.quit()