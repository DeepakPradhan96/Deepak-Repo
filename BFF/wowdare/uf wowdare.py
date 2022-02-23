from selenium import webdriver
import time
from  selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#import org.openqa.selenium.JavascriptExecutor

driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get('https://wowdare.xyz/en/accept/srQRF')
driver.maximize_window()

driver.find_elements_by_name('name')[0].send_keys('Test')
time.sleep(2)
driver.find_elements_by_css_selector('.btn.primary-btn.start.mt-4.w-90')[0].click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="197"]')[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="160"]')[0].click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="Blue"]').click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="46"]')[0].click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="Beautiful Life Partner"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[data-file-id="164"').click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'div[value="Action"]').click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[data-file-id="194"]').click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[data-file-id="144"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="A Dinner with family"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[data-file-id="188"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="The Creative One"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[data-file-id="138"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="Two"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[data-file-id="181"]').click()
time.sleep(3)

#wait = WebDriverWait(driver, 10)
#element=wait.until(EC.element_to_be_clickable((By.ID,"'step16")))
#element.click()
#time.sleep(2)

x=driver.find_element_by_id("step16")
driver.execute_script("arguments[0].click()",x)
time.sleep(3)