from selenium.webdriver import Chrome

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains

driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')

driver.get('https://thetestingworld.com')

obj=ActionChains(driver)
#obj.click().perform()#for left click

#obj.double_click(driver.find_element_by_link_text('Login')).perform()

obj.move_to_element(driver.find_element_by_xpath('//*[@id="menu516"]/span')).perform()
# for context_click() Right Click
#obj.context_click().perform()


from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_mouseOperations():

    path="C:\\Users\\TestingWorld\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/")
    act = ActionChains(driver)

    # Click operation
    #act.click().perform()
    #act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    # Context Click(Right Click)
    #act.context_click().perform()
    #act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #act.double_click().perform()
    #act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()



