from selenium.webdriver import Chrome

Path='C:\Driver\chromedriver_win32\chromedriver.exe'
driver = Chrome(executable_path=Path)
driver.get('https://www.naukri.com/')
driver.maximize_window()

all_window=driver.window_handles

for win in all_window:

    driver.switch_to.window(win)
    print(driver.current_url)
    if (driver.current_url=='https://www.naukri.com/'):
     minwin=win

    else:
     driver.close()
driver.switch_to.window(minwin)
print(driver.current_url)

driver.close()
