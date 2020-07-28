from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testxueqiu:
    def setup(self):
        desire_cap = {
            'platformName': 'Android',
            'platformVersion': '6',
            'deviceName':'127.0.0.1:7555',
            'browserName': 'Browser',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'chromedriverExecutable':'E:\\appium\\chromedriver.exe',
        #    'newCommendTimeout': 6000,
#            'dontStopAppOnReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_browser(self):
       self.driver.get('http://m.baidu.com')
       sleep(5)