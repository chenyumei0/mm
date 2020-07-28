from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage


class DelMember(BasePage):
    save_tab=(MobileBy.ID,'com.tencent.wework:id/e3f')
    confirm_tab=(MobileBy.ID,'com.tencent.wework:id/bci')
    def del_member(self):
    #    self.driver.find_element_by_id('com.tencent.wework:id/e3f').click()
        self.find_and_click(self.save_tab)
        # 点击确定
    #    self.driver.find_element_by_id('com.tencent.wework:id/bci').click()
        self.find_and_click(self.confirm_tab)
        from TEST_APPIUM.test_wework.basepage.memberinforpage import MemberInfo
        return MemberInfo(self.driver)