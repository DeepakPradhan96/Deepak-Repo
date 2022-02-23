from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://thetestingworld.com/testings/")
#driver.fullscreen_window()
#Set Window Size

print(driver.get_window_size())
#driver.set_window_rect(x=30, y=300, width=45, height=500)
#driver.set_window_size(500,800)
window_pos= driver.get_window_position()
print(window_pos)

#Searching book name as string/query in search bar
