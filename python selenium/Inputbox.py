import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://www.python.org")
print('assert "Python" in driver.title')#The Python assert keyword tests if a condition is true. If a condition is false, the program will stop with an optional message. ... That's where the Python assert keyword comes in. The assert statement lets you test for a particular condition in Python. It is used commonly during Python debugging to handle errors.
time.sleep(5)
elem = driver.find_element_by_name("q")
time.sleep(5)
print(elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()