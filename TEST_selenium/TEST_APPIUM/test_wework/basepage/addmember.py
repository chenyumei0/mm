'''
添加成员页
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from TEST_APPIUM.test_wework.basepage.basepage import BasePage
from TEST_APPIUM.test_wework.basepage.contantsaddpage import ContanctAddPage


class AddMember(BasePage):
    toast_ele=(MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
    add_member_element=(MobileBy.XPATH,'//*[@text="手动输入添加"]')
    text_toast = (MobileBy.XPATH, '//*[@text="确定"]')
    text_toast2 = (MobileBy.XPATH, '//*[@text="取消"]')
    def add_member(self):
        '''
        手动输入添加
        :return:
        '''
       # self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.find_and_click(self.add_member_element)
        return ContanctAddPage(self.driver)

    def get_toast(self):
        '''
        获取toast
        '''

        # try:
        ele_toast=self.webdriver_wair(self.toast_ele)
        #     # ele_toast = WebDriverWait(self.driver, 10).until(
        #     #     lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        result = ele_toast.text
        return result
        # except:
        #     self.find_and_click(self.text_toast)
        #     self.back()
        #     self.find_and_click(self.text_toast2)
        #     self.back()


