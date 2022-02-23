import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time


driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

driver.find_elements_by_xpath("//*[@id='Tabbed']/a/button")[0].click() #give the path of button with click() Atribute

time.sleep(3)

#driver.close() #close() cmd only close one tab/Broswer At a time

driver.quit()  # it close All The Broswer

