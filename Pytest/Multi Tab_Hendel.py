from selenium.webdriver import Chrome

Path='C:\Driver\chromedriver_win32\chromedriver.exe'
driver = Chrome(executable_path=Path)
driver.get('https://thetestingworld.com/testings/')
driver.maximize_window()

driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys('test')
driver.find_element_by_name('_txtPassword').send_keys('test')
driver.find_element_by_xpath("//input[@value='Login' and @type='submit']").click()
driver.find_element_by_css_selector('.dropdown-toggle').click()
driver.find_element_by_xpath("//li[@class='dropdown open']//ul[@class='dropdown-menu']//li//a[@href='manage_customer.php'][normalize-space()='Delete']").click()

all_tab=driver.window_handles
print(driver.current_url)

for tab in all_tab:
    driver.switch_to.window(tab)
    print(driver.current_url)



driver.find_element_by_css_selector('#downloadButton').click()

