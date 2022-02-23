import time

from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')

driver.get('https://thetestingworld.com/testings/')
driver.find_element_by_name('fld_username').send_keys('Deepak')

obj=ActionChains(driver)
obj.key_down(Keys.CONTROL).send_keys('a').key_down(Keys.CONTROL).send_keys('c').perform()
time.sleep(4)
driver.find_element_by_name('fld_email').click()

time.sleep(1)
obj.key_down(Keys.CONTROL).send_keys('v').perform()