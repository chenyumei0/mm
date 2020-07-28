
from appium.webdriver.common.mobileby import MobileBy

from TEST_APPIUM.test_wework.basepage.addmember import AddMember
from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.searchmember import SearchMember


class ContanctPage(BasePage):
    '''
    通讯录列表页
    '''
    add_member_text="添加成员"
    search_tab=(MobileBy.ID, 'com.tencent.wework:id/h9z')
    def add_contanct(self):
        '''
        点击添加成员
        :return:
        '''
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().'
        #                                                 'text("添加成员").instance(0));').click()
        self.find_by_scroll(self.add_member_text).click()
        return AddMember(self.driver)
    def search_contanct(self):
        '''
        点击搜索
        :return:
        '''
        self.find_and_click(self.search_tab)
        return SearchMember(self.driver)