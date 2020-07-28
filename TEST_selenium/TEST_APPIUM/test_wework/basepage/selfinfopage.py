from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.eiditpage import EditMember


class SelfInfo(BasePage):
    tab_name=(MobileBy.ID,'com.tencent.wework:id/h9p')
    def goto_edit(self):
        sleep(3)
        #self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h9p').click()
        self.find_and_click(self.tab_name)
        return EditMember(self.driver)