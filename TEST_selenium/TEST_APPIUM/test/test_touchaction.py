from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_touchaction:
    def setup(self):
        desire_cap={
            'platformName': 'Android',
            'platformVersion': '6',
            'deviceName': 'MUMU',
            'appPackage': 'com.android.settings',
            'appActivity': '.Settings',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'newCommendTimeout': 6000,
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
        self.driver.implicitly_wait(10)
    def teardown(self):
       # self.driver.quit()
        pass
    def test_touch_action(self):
        print('解密码锁')
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        self.driver.find_element_by_xpath("//*[@resource-id = 'com.android.settings:id/title' and @text ='安全']").click()
        self.driver.find_element_by_xpath("//*[@resource-id = 'android:id/title' and @text ='屏幕锁定方式']").click()
        self.driver.find_element_by_xpath("//*[@resource-id = 'android:id/title' and @text ='图案']").click()
        action.press(x=120,y=450).move_to(x=360,y=450).move_to(x=600,y=450).move_to(x=600,y=690).move_to(x=600,y=930).release().perform()
