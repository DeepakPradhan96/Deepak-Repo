from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#driver.get('https://bff.lolzz.me/en')
#driver.get('https://bffstag.lolzz.me/en')

driver.get('https://bff.lolzz.me/my/accept/dY78i')


driver.find_elements_by_name('name')[0].send_keys('Deepak')
time.sleep(0)

driver.find_elements_by_xpath('/html/body/div/div[2]/div[3]/div/div[4]/a')[0].click()

time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="329"]')[0].click() #Q1
time.sleep(5)

#driver.find_element_by_id('onesignal-slidedown-allow-button').click()
#time.sleep(2)

wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,1400)","")#auto scroll cmd
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="338"]')[0].click() #Q2
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'div[value="Melepak dengan kawan-kawan"]').click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="343"]')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="35-40"]').click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="322"]')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="Menyelam"]').click()#Q7
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="349"]')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="Empat"]').click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="356"]')[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="361"]')[0].click()
time.sleep(2)
driver.find_elements_by_css_selector("div[value='Perjalanan masa']")[0].click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="365"]')[0].click()

time.sleep(2)
driver.find_elements_by_css_selector("div[value='Mei']")[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="382"]')[0].click()

time.sleep(2)