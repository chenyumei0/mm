from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    search = driver.find_element(By.ID,'su').get_attribute('value')
    assert search == '百度一下'


