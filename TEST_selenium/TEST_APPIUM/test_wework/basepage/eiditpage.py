from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.delmemberpage import DelMember


class EditMember(BasePage):

    eidti=(MobileBy.XPATH,'//*[@text="编辑成员"]')
    def goto_delmember(self):
        sleep(2)
       # self.driver.find_element(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        self.find_and_click(self.eidti)
        return DelMember(self.driver)
