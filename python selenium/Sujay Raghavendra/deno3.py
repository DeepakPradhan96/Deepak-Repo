from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get('https://thetestingworld.com/testings/')

x=driver.find_elements_by_class_name('displayPopup').get_attribute('Read Detail')
print(x)






ActionChains(driver)\
.key_down(Keys.CONTROL)\
.send_keys("a")\
.key_up(Keys.CONTROL)\
.key_down(Keys.CONTROL)\
.send_keys("c")\
.key_up(Keys.CONTROL)\
.perform()