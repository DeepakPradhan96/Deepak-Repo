from selenium.webdriver import Chrome
import pytest

# a=10
@pytest.fixture()#scope="module")  is use only one Before all
def setpath():
    global driver
    Path='C:\Driver\chromedriver_win32\chromedriver.exe'
    driver = Chrome(executable_path=Path)
    yield #use After All
    driver.close()

def test_Registation_Valid_data(setpath):
   driver.get('https://thetestingworld.com/testings/')


   assert driver.current_url=='https://thetestingworld.com/testings/'

#@pytest.mark.skipif(a>100,reason='less 100 skip it')

def test_Registation_inValid_data(setpath):

   driver.get('https://thetestingworld.com/testings/')
   driver.maximize_window()

def test_inValid_data(setpath):

   driver.get('https://thetestingworld.com/testings/')
   driver.maximize_window()