from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
action = ActionChains(driver)
action.send_keys()
action.click(on_element=None)
action.click_and_hold(on_element=None)
action.context_click(on_element=None)
action.double_click()
action.drag_and_drop(source=0,target=1)
action.drag_and_drop_by_offset(source=1,xoffset=1,yoffset=2)
action.key_down(value=0,element=None)
action.key_up(value=0,element=None)
#按下Ctrl+C并且释放
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

action.move_by_offset(10,20)
action.move_to_element(to_element='x')

action.move_to_element_with_offset(to_element='x',xoffset=1,yoffset=2)
action.perform()
action.release(on_element='c')
