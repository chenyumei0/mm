import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('https://home.testing-studio.com')
        category_name=(By.CSS_SELECTOR,'#ember185 .category-name')
        self.driver.find_element(By.LINK_TEXT,'所有分类').click()
        WebDriverWait(self.driver,10).until(
            expected_conditions.element_to_be_clickable(category_name)
        )
        self.driver.find_element(*category_name).click()

    def test_baidu(self):
        self.driver.get('http://www.baidu.com')
        self.driver.refresh()
        print(self.driver.page_source)
        search = self.driver.find_element(By.ID,'su')
        print(search.size,search.location,search.get_attribute('value'))
