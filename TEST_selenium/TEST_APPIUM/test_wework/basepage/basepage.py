import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

'''
用来存放一些基本的方法
'''
class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver=None):
        self.driver=driver
    #查找元素
    def find(self,locator):
        logging.info(f'find:{locator}')
        return self.driver.find_element(*locator)
    #查找多个元素
    def finds(self,locator):
        logging.info(f'finds:{locator}')
        return self.driver.find_elements(*locator)

    #查找并点击元素
    def find_and_click(self,locator):
        logging.info(f'clic')
        self.find(locator).click()

    #查找元素并输入值
    def find_and_sendkeys(self,locator,keys):
        logging.info(f'sendkeys:{locator}')
        self.find(locator).send_keys(keys)

    #滚动查找
    def find_by_scroll(self,text):
        logging.info(f'find_by_scroll')
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        f'text("{text}").instance(0));')

    #显示等待
    def webdriver_wair(self,locator,timeout=10):
        logging.info(f'webdriver_wait:{locator}')
        ele_toast = WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(*locator))
        return ele_toast

    def back(self,num=1):
        for i in range(num):
            self.driver.back()