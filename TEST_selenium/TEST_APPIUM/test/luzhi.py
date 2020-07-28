from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testxueqiu:
    def setup(self):
        desire_cap = {
            'platformName': 'Android',
            'platformVersion': '6',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.common.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'newCommendTimeout': 6000,
#            'dontStopAppOnReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_xueqiu1(self):

        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
        el3.click()
        self.driver.back()

    # This sample code uses the Appium python client
    # pip install Appium-Python-Client
    # Then you can paste this into a file and simply run with Python
    def test_xueqiu2(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout").click()


    def test_xueqiu3(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text= '阿里巴巴']").click()
        current_price=float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price >200
        #self.driver.back()

    def test_touch_action(self):
        action = TouchAction(self.driver)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        window_rect =self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height*4/5)
        y_end = int(height/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_currentprice(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@text='阿里巴巴' and @resource-id='com.xueqiu.android:id/name']").click()
        current_price_HK=self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert float(current_price_HK)>200

    def test_login(self):
        '''
        1.点击我的
        2.点击登录雪球
        3.输入用户名密码
        4.点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('abcdef')
        button=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.xueqiu.android:id/button_next")')
        ele=WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(button))
        ele.click()
        sleep(5)

    def test_scroll(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("快乐魔兽").instance(0));').click()


    def test_jijin(self):

        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        #切换上下文
       # self.driver.switch_to.context(self.driver.contexts[-1])
        #点击A股开户
        self.driver.find_element(MobileBy.XPATH,'//*[@content-desc=	"A股开户"]').click()
        # 切换窗口

        #显示等待
        phonenumber = (MobileBy.ID,'phone-number')
        WebDriverWait(self.driver,120).until(expected_conditions.element_to_be_clickable(phonenumber))
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)
        #输入用户名密码
        self.driver.find_element(*phonenumber).send_keys('11111111111')
        self.driver.find_element(MobileBy.ID,'code').send_keys('1234')
        self.driver.find_element(MobileBy.XPATH,'//*[@content-desc="立即开户"]').click()

    def test_mobile(self):
        self.driver.make_gsm_call('18700460110',GsmCallActions.CALL)
        self.driver.send_sms('13636761245','are you ok')


if __name__ == '__main__':
    pytest.main()