from selenium import webdriver
import time
from  selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
#from selenium.webdriver.common.keys import keys, Keys
import pyperclip

driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get('https://wowdare.xyz/cn')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys("test")
driver.find_elements_by_css_selector('.btn.primary-btn.start.mt-4.w-90')[0].click()
time.sleep(0.3)


driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.implicitly_wait(10)
assert driver.find_element_by_css_selector(By.CSS_SELECTOR,'#').click(),"not clickble"

time.sleep(2)




driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)


driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(0.3)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()
time.sleep(0.5)
for x in range(0,12):
    skip = driver.find_element_by_class_name('skip').click()
    time.sleep(0)
    if x==10:
        print(x)
        break

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()

time.sleep(3)

driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_css_selector('button[title="Copy Link"]').click()
time.sleep(3)

'''chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--incognito")
y=webdriver.Chrome(chrome_options=chrome_option)
y.maximize_window()
y.get("https://www.google.com/")
time.sleep(3)

act=ActionChains(y)
url=pyperclip.paste()
print(url)

y.execute_script("window.open(\""+url+"\")")
#driver.execute_script("window.open(\""+url+"\")")

handle=y.window_handles
for win in handle:
     y.switch_to.window(win)
     if (y.title=='Best Friends Cup'):
      print(y.current_url)

wait = WebDriverWait(y, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "onesignal-slidedown-allow-button")))
element.click()
time.sleep(1)

y.find_element_by_name("name").send_keys("test@gmail.com")

y.find_element_by_xpath("//a[text()='Start']").click()
time.sleep(3)
y.find_element_by_name('name').clear()

y.find_element_by_name('name').send_keys('Deepak123#')

y.find_element_by_xpath("//a[text()='Start']").click()'''


