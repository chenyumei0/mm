import os
from selenium import webdriver

def Base():
    browser = os.getenv('browser')
    if browser == 'headless':
        driver = webdriver.PhantomJS()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()