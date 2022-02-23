from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get('https://meelo.me/')

driver.find_elements_by_name('name')[0].send_keys('Test2')
time.sleep(2)

wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
time.sleep(2)
driver.find_elements_by_class_name('tflat-edit')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"span[class='tflat-wrong font-weight-bold']").click()
time.sleep(2)

driver.find_elements_by_class_name('tflat-edit')[0].click()
time.sleep(2)
driver.find_elements_by_name('custom')[0].send_keys('what is your Mother Tong?')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"span[class='tflat-tick font-weight-bold']").click()
time.sleep(4)

for x in range(0,20):
    question=driver.find_element(By.CSS_SELECTOR,"span[class='tflat-shuffle']").click()
    time.sleep(1)
    if x==1:
        print(x)
        break
time.sleep(2)

for x in range(0,10):
    question=driver.find_element(By.CSS_SELECTOR,"a[class='tch-hover shuffle-color']").click()
    time.sleep(1)
    if x==5:
        print(x)
        break
time.sleep(2)

for x in range(0,10):
    question=driver.find_element(By.CSS_SELECTOR,"span[class='tflat-boy']").click()
    time.sleep(1)
    if x==5:
        print(x)
        break
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"span[class='tflat-unlock']").click()
time.sleep(2)
driver.find_element_by_id('yes').click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"span[class='tflat-lock']").click()
time.sleep(2)
driver.find_element_by_id('yes').click()
time.sleep(2)

driver.find_elements_by_xpath("//button[normalize-space()='Save & Share']")[0].click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
open=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class='fa fa-eye text-white']")))
open.click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
#element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class='aria-hidden']")))
close=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'close')))
close.click()
time.sleep(2)

link=driver.find_element(By.CSS_SELECTOR,'button[title="Copy Link"]')
driver.execute_script('arguments[0].click()',link)

from selenium import webdriver
#chorme_option=webdriver.ChromeOptions()
#chorme_option.add_argument("--incognito")

#driver=webdriver.Chrome(chrome_options=chorme_option)
#driver.get('https://meelo.me/Test28686/q1')

y=webdriver.Firefox()
y.maximize_window()
y.get('https://meelo.me/Test25450/q1')
y.quit()