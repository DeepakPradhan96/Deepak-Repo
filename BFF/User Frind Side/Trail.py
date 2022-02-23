from selenium import webdriver
import time
from  selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import keys, Keys
y=webdriver.Firefox()
y.maximize_window()
y.get('https://www.google.com/')

y.find_elements_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')[0].send_keys('yyyu')