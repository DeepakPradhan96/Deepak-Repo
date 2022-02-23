from selenium.webdriver import Chrome

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains

driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')

driver.get('https://thetestingworld.com')

obj=ActionChains(driver)
#obj.click().perform()#for left click

#obj.double_click(driver.find_element_by_link_text('Login')).perform()

obj.move_to_element(driver.find_element_by_xpath('//*[@id="menu516"]/span')).perform()
# for context_click() Right Click
#obj.context_click().perform()



