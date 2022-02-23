from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver= webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/V1/index.php")

uid_ele=driver.find_element_by_name("uid")

print(uid_ele.is_displayed()) #return Element Status true/falase

print(uid_ele.is_enabled()) #return Enable/disable Status true/falase

pwd_ele=driver.find_element_by_name("password")

print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

uid_ele.send_keys("mngr344767")

pwd_ele.send_keys("yvynasa")

driver.find_element_by_name("btnLogin").click()

time.sleep(2)

x=driver.find_elements_by_xpath("/html/body/div[3]/div/ul/li[2]/a")[0].click()
print(x)
radio = driver.find_elements_by_css_selector("input[name=rad1]")

