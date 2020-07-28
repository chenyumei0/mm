'''
手动添加成员页
'''
#from TEST_APPIUM.test_wework.basepage.addmember import AddMember
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage


class ContanctAddPage(BasePage):
    add_name=(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@text="必填"]')
    add_gender=(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]')
    meal_ele=(MobileBy.XPATH,'//*[@text="男"]')
    femeale_ele=(MobileBy.XPATH,'//*[@text="女"]')
    add_phonenumber=(MobileBy.XPATH,'//*[@text="手机号"]')
    save_element=(MobileBy.XPATH,'//*[@text="保存"]')
    def set_name(self,name):
        '''
        输入姓名
        :param name:
        :return:
        '''

     #   self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys(name)
        self.find_and_sendkeys(self.add_name,name)
        return self
    def set_gender(self,gender):
        '''
        输入性别
        :param gender:
        :return:
        '''
        sleep(1)
        #self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        self.find_and_click(self.add_gender)
        if gender == '男':
            #self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]').click()
            self.find_and_click(self.meal_ele)
        else:
            #self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
            self.find_and_click(self.femeale_ele)
        return self
    def set_phonenumber(self,phonenumber):
        '''
        输入电话号码
        :param phonenumber:
        :return:
        '''
     #   self.driver.find_element(MobileBy.XPATH,'//*[@text="手机号"]').send_keys(phonenumber)
        self.find_and_sendkeys(self.add_phonenumber,phonenumber)
        return self
    def click_save(self):
        '''
        点击保存
        :return:
        '''
    #    self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()
        self.find_and_click(self.save_element)
        from TEST_APPIUM.test_wework.basepage.addmember import AddMember
        return AddMember(self.driver)
