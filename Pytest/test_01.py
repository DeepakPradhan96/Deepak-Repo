from selenium.webdriver import Chrome
import pytest

# a=10
@pytest.mark.sanity   #decorater
def test_Registation_Valid_data():
   driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
   driver.get('https://thetestingworld.com/testings/')

#@pytest.mark.skipif(a>100,reason='less 100 skip it')
@pytest.mark.Smoke
def test_Registation_inValid_data():
   driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
   driver.get('https://thetestingworld.com/testings/')
   driver.maximize_window()
@pytest.mark.sanity
def test_inValid_data():
   driver=Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
   driver.get('https://thetestingworld.com/testings/')
   driver.maximize_window()

# python -m pytest -v -s
#python -m pytest -k test_Registation_Valid_data

# python -m pytest -m sanity

# python -m pytest -m "not sanity"
