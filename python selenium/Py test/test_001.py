from selenium.webdriver import Chrome
import pytest
a=10
def test_Registation_Valid_data():
   driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
   driver.get('https://thetestingworld.com/testings/')

@pytest.mark.skip(a>100,'skip it')
def test_Registation_inValid_data():
   driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
   driver.get('https://thetestingworld.com/testings/')
   driver.maximize_window()


