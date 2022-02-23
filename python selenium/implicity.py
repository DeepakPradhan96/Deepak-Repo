from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get('http://demo.guru99.com/V1/index.php')

driver.implicitly_wait(10) #implicitly_wait() cmd applycable onn all element of program #it is time base

driver.find_element_by_name('uid').send_keys('mngr344767')
driver.find_element_by_name('password').send_keys('yvynasa')

driver.find_element_by_name('btnLogin').click()



