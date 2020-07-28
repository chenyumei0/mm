'''
搜索页
'''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.memberinforpage import MemberInfo


class SearchMember(BasePage):
    inputInfo = (MobileBy.ID, 'com.tencent.wework:id/fxc')
    def goto_search(self,name):
        #self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fxc').send_keys(name)
        self.find_and_sendkeys(self.inputInfo,name)

        return MemberInfo(self.driver)