from selenium import webdriver

from selenium.webdriver.common.keys import Keys

x=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")#lunch the Chrome Broswer

#Exucute code on Broswer
x.get("https://heymates.me/heymates")

print(x.title)# print The Title Of Page

print(x.current_url)#print The  Url of Page

print(x.page_source)#print The Html Code Of  page

x.close()