from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get('https://thetestingworld.com/testings/')

'''print(driver.title)
print(driver.current_url)
print(driver.page_source)'''

obj=Select(driver.find_element_by_name('sex'))
obj.select_by_index(2)
print(obj.first_selected_option.text)

for i in obj.options:
    print(i.text)




