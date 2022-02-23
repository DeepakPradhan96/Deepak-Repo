from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
y=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
y.get("http://www.google.com/")


act=ActionChains(y)
url="https://bff.lolzz.me/en/accept/4xdPg"
print(url)

y.execute_script("window.open(\""+url+"\")")
#driver.execute_script("window.open(\""+url+"\")")

handle=y.window_handles
for win in handle:
    y.switch_to.window(win)
    if (y.title=="Best Friends Cup"):
     print(y.current_url)

y.find_elements_by_name('name')[0].send_keys('Deepak')
time.sleep(2)



