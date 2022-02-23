from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
from  selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#driver.get('https://bff.lolzz.me/en')
#driver.get('https://bffstag.lolzz.me/en')

driver.get('https://bff.lolzz.me/ch')


driver.find_elements_by_name('name')[0].send_keys('Deepak')
time.sleep(0)

driver.find_elements_by_xpath('/html/body/div/div[2]/div[3]/div/div[4]/a')[0].click()

time.sleep(2)

wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="329"]')[0].click() #Q1
time.sleep(5)

#driver.find_element_by_id('onesignal-slidedown-allow-button').click()
#time.sleep(2)


driver.execute_script("window.scrollBy(0,900)","")#auto scroll cmd
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="338"]')[0].click() #Q2
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'div[value="與父母討論"]').click()

time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="343"]')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="35-40"]').click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="322"]')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="潛水"]').click()#Q7
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="349"]')[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="三種"]').click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="356"]')[0].click()
time.sleep(2)

driver.find_elements_by_css_selector('div[data-file-id="361"]')[0].click()
time.sleep(2)
driver.find_elements_by_css_selector("div[value='時間旅行']")[0].click()
time.sleep(2)
driver.find_elements_by_css_selector('div[data-file-id="365"]')[0].click()

time.sleep(2)
driver.find_elements_by_css_selector("div[value='三月']")[0].click()
time.sleep(2)



for x in range(0,13):
    skip = driver.find_elements_by_class_name('skip')[0].click()
    time.sleep(1)
    if x==9:
        print(x)
        break

driver.find_elements_by_css_selector('div[data-file-id="382"]')[0].click()
time.sleep(2)

link=driver.find_element(By.CSS_SELECTOR,'button[title="Copy Link"]')
driver.execute_script('arguments[0].click()',link)

time.sleep(3)

