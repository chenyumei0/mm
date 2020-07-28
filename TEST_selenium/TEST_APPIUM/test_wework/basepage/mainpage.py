from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.contantspage import ContanctPage
from TEST_APPIUM.test_wework.basepage.workbench import WorkBench


class MainPage(BasePage):
    contacts_tab=(MobileBy.XPATH,'//*[@text="通讯录"]')
    work_bench_tab=(MobileBy.XPATH,"//*[@text='工作台']")
    #消息
    def message(self):
        pass

    #进入到通讯录
    def goto_contancs(self):
        self.find_and_click(self.contacts_tab)
#        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return ContanctPage(self.driver)

    #进入到工作台
    def goto_workbench(self):
        self.find_and_click(self.work_bench_tab)
 #       self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        return WorkBench()
    #我
    def goto_mine(self):
        pass