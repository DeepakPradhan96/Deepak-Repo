
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver=Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get('https://thetestingworld.com/testings/')
driver.maximize_window()

#Enter data to textbox
driver.find_elements_by_name('fld_username')[0].send_keys('Deepak')
driver.find_elements_by_xpath("//input[@name='fld_email']")[0].send_keys('deepak@gmailcom')
time.sleep(2)
driver.find_elements_by_name('fld_username')[0].clear()
driver.find_elements_by_name('fld_username')[0].send_keys('deepak123')
driver.find_elements_by_xpath("//input[@value='home']")[0].click()
#work On Drop Down
obj=driver.find_element_by_name('sex') #s is issue
drpdown=Select(obj)
drpdown.select_by_index(2)
time.sleep(3)
drpdown.select_by_visible_text('Male')
drpdown.select_by_value()
