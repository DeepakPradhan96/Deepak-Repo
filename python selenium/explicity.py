from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
import time


driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://www.expedia.com/')

driver.find_element(By.LINK_TEXT,'Flights').click()
#driver.find_element_by_partial_link_text('ghts').click()

driver.find_element_by_link_text('Roundtrip').click()
driver.find_elements_by_css_selector('button[aria-label="Leaving from"]')[0].send_keys('NYC')

time.sleep(3)
driver.find_elements_by_css_selector('button[aria-label="Going to San Francisco (SFO - San Francisco Intl.)"]')


#driver.find_element_by_id('d1-btn').clear()
driver.find_element_by_id('d1-btn').send_keys('17/08/2021')

#driver.find_element_by_id('d2-btn').clear()
driver.find_element_by_id('d2-btn').send_keys('21/08/2021')

time.sleep(3)
driver.find_elements_by_css_selector('button[data-testid="submit-button"]')[0].click()





