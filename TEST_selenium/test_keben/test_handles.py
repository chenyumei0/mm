from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.find_element(By.ID,'kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element(By.ID,'su').click()
        self.driver.find_element(By.LINK_TEXT,'霍格沃兹测试学院_腾讯课堂').click()
        sleep(5)
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element(By.CSS_SELECTOR,'名企定向培养').click()