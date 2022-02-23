from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
y=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
y.get("https://wowdare.xyz/en/share")
print(y.title)