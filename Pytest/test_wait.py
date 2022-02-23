from selenium.webdriver import Chrome
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions  as Ec
from selenium.webdriver.common.by import By
@pytest.fixture()#scope="module")  is use only one
def setpath():
    global driver
    Path='C:\Driver\chromedriver_win32\chromedriver.exe'
    driver = Chrome(executable_path=Path)
    #driver.implicitly_wait(10)
    driver.get('https://thetestingworld.com/testings/')


def test_Registation_Valid_data(setpath):
    wait = WebDriverWait(driver, 100)
    ele=wait.until(Ec.text_to_be_present_in_element((By.ID,'countryId'),'India'))

    obj=Select(driver.find_element_by_id('countryId'))
    obj.select_by_visible_text('India')

    wait=WebDriverWait(driver,100)
    ele=wait.until(Ec.text_to_be_present_in_element((By.ID ,'stateId'),'Odisha'))
    obj=Select(driver.find_element_by_id('stateId'))
    obj.select_by_visible_text('Odisha')


