from selenium import webdriver
from selenium.webdriver.common.keys import keys

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")#lunch the Chrome Broswer
#driver=webdriver.Firefox(executable_path="C:\Driver\geckodriver-v0.29.1-win64\geckodriver.exe") #lunch the Fire Fox broswer

#driver=webdriver.Ie(executable_path="C:\Driver\IEDriverServer_Win32_3.150.1\IEDriverServer.exe")

#Exucute code on Broswer

driver.get("https://heymates.me/heymates")

print(driver.title)#titel Of the Page

driver.close()#close The Broswer


