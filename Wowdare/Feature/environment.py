from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium import webdriver
#context= global/use entair project

def before_all(context):
    path='C:\\Driver\\chromedriver_win32\\chromedriver.exe'
    context.driver =Chrome(executable_path=path)

    Path="C:\\Driver\\geckodriver-v0.29.1-win64\\geckodriver.exe"

    context.driver2=Firefox(executable_path=Path)


def after_all(context):
    context.driver.close()
