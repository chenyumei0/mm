#启动
from appium import webdriver

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.mainpage import MainPage
#存放APP常用的一些方法
class APP(BasePage):
    #启动APP
    def start(self):
        if self.driver ==None:
            caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "platformVersion": "6",
                'appPackage': 'com.tencent.wework',
                'appActivity': '.launch.LaunchSplashActivity',
                'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
                'resetKeyboard': True,  # 执行完程序恢复原来输入法
                'noReset': True,  # 不要重置App
                'newCommandTimeout': 6000,
                'automationName': 'UiAutomator2'
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self
    #重启APP
    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        return self
    #停止APP
    def stop(self):
        self.driver.quit()

    #进入主页
    def goto_main(self):
        return MainPage(self.driver)