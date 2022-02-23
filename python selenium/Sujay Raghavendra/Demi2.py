from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#Open apress webpage
driver.get('https://apress.com')
#Open Google page
driver.get('https://google.com')

# Different Navigation command in selenium

driver.back()
driver.forward()
driver.refresh()
print("Moved to first page")




