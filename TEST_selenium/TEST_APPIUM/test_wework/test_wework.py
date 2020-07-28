# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


with open('testdatas/member_data.yml',encoding='utf-8') as f:
    datas=yaml.safe_load(f)
    myids_add=datas['add'].keys()
    mydatas_add=datas['add'].values()

    myids_del=datas['del'].keys()
    mydatas_del=datas['del'].values()
class Testwework:
    def setup_class(self):
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
        self.driver.implicitly_wait(10)
    def teardown_class(self):
        self.driver.quit()

    def test_wework(self):
        print('测试企业微信打卡')
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                                'scrollable(true).instance(0)).'
                                                                'scrollIntoView(new UiSelector().'
                                                                'text("打卡").instance(0));').click()
    #driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/gw8' and @text='外出打卡']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ao_").click()

        self.driver.back()

    #@pytest.mark.parametrize('name,phonenumber,gender', mydatas_add, ids=myids_add)
    #, name, phonenumber, gender
    def test_addmember(self):
        name='aaa1'
        gender='男'
        phonenumber='11111111112'
        print(f'测试企业微信添加成员，添加{name}')
        #进入通讯录页面
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        #点击添加成员
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                                'scrollable(true).instance(0)).'
                                                                'scrollIntoView(new UiSelector().'
                                                                'text("添加成员").instance(0));').click()
        #选择手动添加用户
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        #填入用户信息
        self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        if gender == '男':
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()

        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(phonenumber)
        self.driver.find_element_by_xpath('//*[@text="设置部门"]').click()
        #点击确定
        self.driver.find_element_by_xpath('//*[@text="确定(1)"]').click()
        #点击保存
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()
       # self.driver.find_element_by_xpath('//*[class="android.widget.Toast"]')
        ele_toast = WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]'))
        result = ele_toast.text
        assert "成功" in result
        self.driver.back()

   # @pytest.mark.parametrize('name',mydatas_del,ids=myids_del)
    def test_del_member(self):
        name = 'aaa'
        print(f'测试企业微信删除成员,删除{name}')
        #进入通讯录界面
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #找到要删除的成员
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h9z').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/fxc').send_keys(name)
        sleep(2)
        elements=self.driver.find_elements(MobileBy.XPATH,f'//*[@text="{name}"]')
        if len(elements)<2:
            print('没有这个联系人')
        elements[1].click()
        # self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
        #                                                 f'scrollable(true).instance(0)).'
        #                                                 f'scrollIntoView(new UiSelector().'
        #                                                 f'text("{name}").instance(0));').click()
        #点击右上角设置按钮
        self.driver.find_element_by_id('com.tencent.wework:id/h9p').click()
        #点击编辑成员
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        #点击删除成员
        self.driver.find_element_by_id('com.tencent.wework:id/e3f').click()
        #点击确定
        self.driver.find_element_by_id('com.tencent.wework:id/bci').click()
        sleep(2)

        elelist_after = self.driver.find_elements_by_xpath(f'//*[@text="{name}"]')
        assert len(elelist_after) ==len(elements)- 1
        print('删除联系人成功')




