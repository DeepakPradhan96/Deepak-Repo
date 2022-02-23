from selenium.webdriver import Chrome
#import TakeScreenshoot

Path='C:\Driver\chromedriver_win32\chromedriver.exe'
driver = Chrome(executable_path=Path)
driver.get('https://thetestingworld.com/testings/')
driver.maximize_window()
#driver.get_screenshot_as_file('C:/Users/deepaak/PycharmProjects/Pytest/SS.png')
#driver.get_screenshot_as_png()