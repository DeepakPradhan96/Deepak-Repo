
import time
from selenium.webdriver import Chrome
import pytest
from webdriver_manager.chrome import ChromeDriverManager
# a=10
@pytest.fixture()#scope="module")  is use only one
def setpath():
    global driver
    Path='C:\Driver\chromedriver_win32\chromedriver.exe'
    driver = Chrome(executable_path=Path)
    driver.get('https://thetestingworld.com/testings/')
    yield
    driver.close()

def test_login(setpath):
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys('test')
    driver.find_element_by_name('_txtPassword').send_keys('test')
    driver.find_element_by_xpath("//input[@value='Login' and @type='submit']").click()
    driver.find_element_by_css_selector('.dropdown-toggle').click()
    driver.find_element_by_xpath("//a[text()='Update']").click()
    #driver.find_element_by_xpath("//button[text()='Start Download']")

    time.sleep(5)

    all_win=driver.window_handles
    mainwin=""

    for win in all_win:
            driver.switch_to.window(win)
            print(driver.current_url)


            if (driver.current_url=='https://thetestingworld.com/testings/manage_customer.php'):
                driver.find_element_by_xpath("//button[text()='Start Download']").click()


            elif (driver.current_url=='https://thetestingworld.com/testings/dashboard.php'):
              mainwin=win
              print(driver.current_url)
              #driver.find_element_by_xpath("//a[text()='Report Chart']").click()



    '''driver.switch_to.window(win)
    print(driver.current_url)'''





