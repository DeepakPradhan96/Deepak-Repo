from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#driver.get('https://bff.lolzz.me/en')
driver.get('https://bffstag.lolzz.me/en')

#driver.get('https://bff.lolzz.me/my')

driver.find_elements_by_name('name')[0].send_keys('Test')

driver.find_elements_by_xpath('/html/body/div/div[2]/div[3]/div/div[4]/a')[0].click()

time.sleep(2)

driver.find_elements_by_xpath("//div[normalize-space()='Rolls Royce']//img")[0].click()
time.sleep(2)
wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)

driver.find_elements_by_xpath("//div[normalize-space()='Starbucks']//img")[0].click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'div[value="Distract yourself with a movie"]').click()
time.sleep(2)
driver.find_elements_by_xpath("//div[normalize-space()='Sun Hat']//img")[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="35-40"]').click()
time.sleep(2)
driver.find_elements_by_xpath("//div[normalize-space()='Cycling']//img")[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="Fly in a private Plan"]').click()
time.sleep(2)
driver.find_elements_by_xpath("//div[normalize-space()='Mischievous']//img")[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[value="More than four"]').click()
time.sleep(2)
driver.find_elements_by_xpath("//div[normalize-space()='Cat Eye']//img")[0].click()
time.sleep(2)

driver.find_elements_by_xpath("//div[normalize-space()='Keys']//img")[0].click()
time.sleep(2)
driver.find_elements_by_css_selector("div[value='Flight']")[0].click()
time.sleep(2)
driver.find_elements_by_xpath("//div[normalize-space()='Watching TV']//img")[0].click()
time.sleep(2)
driver.find_elements_by_css_selector("div[value='May']")[0].click()
time.sleep(2)
skip = driver.find_elements_by_class_name('skip')[0].click()
time.sleep(2)

for x in range(0,13):
    skip = driver.find_elements_by_class_name('skip')[0].click()
    time.sleep(1)
    if x==9:
        print(x)
        break


driver.find_elements_by_css_selector('div[data-file-id="380"]')[0].click()
time.sleep(2)

driver.find_elements_by_class_name('sh-whatsapp')[0].click()

#elemment=driver.find_element(By.CSS_SELECTOR,'button[title="Copy Link"]')
#action=ActionChains(driver)

#action.double_click(elemment).perform()

link=driver.find_element(By.CSS_SELECTOR,'button[title="Copy Link"]')
driver.execute_script('arguments[0].click()',link)

time.sleep(3)