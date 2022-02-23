from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#driver.get('https://bff.lolzz.me/en')
#driver.get('https://bffstag.lolzz.me/en')

driver.get('https://bff.lolzz.me/cn')


driver.find_elements_by_name('name')[0].send_keys('Deepak')
time.sleep(0)

driver.find_elements_by_xpath('/html/body/div/div[2]/div[3]/div/div[4]/a')[0].click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="顽皮"]').click()
time.sleep(2)

#driver.find_element_by_id('onesignal-slidedown-allow-button').click()
#time.sleep(2)

wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,1400)","")#auto scroll cmd
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="386"]')[0].click() #Q
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="不好"]').click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,'div[value="一个月一次"]').click()
time.sleep(2)


driver.find_elements_by_css_selector('div[data-file-id="394"]')[0].click() #Q
time.sleep(2)


driver.find_elements_by_css_selector('div[data-file-id="320"]')[0].click() #Q
time.sleep(1)


driver.find_elements_by_css_selector('div[data-file-id="398"]')[0].click() #Q
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="332"]')[0].click() #Q
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="340"]')[0].click() #Q
time.sleep(1)


driver.find_element(By.CSS_SELECTOR,'div[value="与父母讨论"]').click()
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="343"]')[0].click() #Q
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,'div[value="25-35"]').click()
time.sleep(1)

driver.find_elements_by_css_selector('div[data-file-id="326"]')[0].click() #Q
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,'div[value="坐游轮"]').click()
time.sleep(1)

for x in range(0,13):
    skip = driver.find_elements_by_class_name('skip')[0].click()
    time.sleep(0)
    if x==10:
        print(x)
        break


driver.find_elements_by_css_selector('div[data-file-id="350"]')[0].click()
time.sleep(4)

#elemment=driver.find_element(By.CSS_SELECTOR,'button[title="Copy Link"]')
#action=ActionChains(driver)

#action.double_click(elemment).perform() er

#driver.find_element(By.CSS_SELECTOR,'button[title="Copy Link"]')[0].
#driver.execute_script('arguments[0].click()',link)

#time.sleep(3)
driver.execute_script("window.scrollTo(0, 700)")
driver.find_elements_by_css_selector('button[title="Copy Link"]')[0].click()
