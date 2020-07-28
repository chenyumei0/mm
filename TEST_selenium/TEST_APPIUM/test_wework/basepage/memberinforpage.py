from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.selfinfopage import SelfInfo


class MemberInfo(BasePage):

    def searchname(self,name):
        sleep(2)
        text = (MobileBy.XPATH, f'//*[@text="{name}"]')
        ele_list=self.finds(text)
        return ele_list
    def goto_memberlist(self,name):
        elements = self.searchname(name)
        if len(elements) < 2:
            print('没有这个联系人')
        elements[1].click()
        return SelfInfo(self.driver)

    def memberlist_after(self,name):
        elements = self.searchname(name)
        text = (MobileBy.XPATH, f'//*[@text="{name}"]')
        sleep(2)
        elements_after = self.finds(text)
        result=len(elements)-len(elements_after)
        return result
