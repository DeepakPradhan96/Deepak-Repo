from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get('https://bond.lolzz.me/en')
driver.find_elements_by_name('name')[0].send_keys('Test2')
time.sleep(2)


wait = WebDriverWait(driver, 20)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

driver.find_elements_by_xpath("//a[normalize-space()='Start']")[0].click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="Read alot"]').click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="402"]')[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="407"]')[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="417"]')[0].click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="420"]')[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="417"]')[0].click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="Using swear words"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="Lavish"]').click()
time.sleep(2)