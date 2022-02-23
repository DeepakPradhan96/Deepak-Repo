from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#driver.get('https://bff.lolzz.me/en')
driver.maximize_window()
time.sleep(2)
driver.get('https://bff.lolzz.me/my')

driver.find_elements_by_name('name')[0].send_keys('Test')

driver.find_elements_by_xpath('/html/body/div/div[2]/div[3]/div/div[4]/a')[0].click()

time.sleep(2)

wait = WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-allow-button")))
element.click()
time.sleep(2)
#driver.find_element_by_id('onesignal-slidedown-allow-button').click()
#time.sleep(2)

driver.implicitly_wait(10)
driver.find_elements_by_xpath("//div[normalize-space()='Rolls Royce']//img")[0].click()#Q1
time.sleep(1)

#driver.find_element_by_id('onesignal-slidedown-allow-button').click()
#time.sleep(2)

driver.find_elements_by_xpath("//div[normalize-space()='Starbucks']//img")[0].click()#Q2
time.sleep(0)

driver.find_element(By.CSS_SELECTOR,'div[value="Lupakan dengan menonton filem"]').click()#Q3
time.sleep(0)
driver.find_elements_by_xpath("//div[normalize-space()='Beanie']//img")[0].click()#Q4
time.sleep(0)
driver.find_element(By.CSS_SELECTOR,'div[value="35-40"]').click()#Q5
time.sleep(0)
driver.find_elements_by_xpath("//div[normalize-space()='Angkat berat']//img")[0].click()#Q6
time.sleep(0)
driver.find_element(By.CSS_SELECTOR,'div[value="Skydiving"]').click()#Q7
time.sleep(0)
driver.find_elements_by_xpath("//div[normalize-space()='Kelakar']//img")[0].click()#Q8
time.sleep(0)
driver.find_element(By.CSS_SELECTOR,'div[value="Dua"]').click()#Q9
time.sleep(0)
driver.find_elements_by_xpath("//*[@id='question-pg']/div[3]/div[2]/div[2]/img")#Q10
time.sleep(0)

driver.find_elements_by_xpath("//*[@id='question-pg']/div[3]/div[2]/div[2]/img")[0].click()#Q11
time.sleep(0)

driver.find_elements_by_xpath("//*[@id='question-pg']/div[3]/div[2]/div[2]/img")[0].click()#Q11
time.sleep(1)
driver.find_element_by_xpath("//div[@data-file-id='361']").click()

driver.find_element_by_css_selector("div[value='Boleh meninggi']").click()#Q12
time.sleep(0)
driver.find_elements_by_xpath("//*[@id='question-pg']/div[3]/div[2]/div[2]/img")[0].click()#Q13
time.sleep(0)

driver.find_elements_by_css_selector("div[value='Februari']")[0].click()#Q14
time.sleep(0)

skip = driver.find_elements_by_class_name('skip')[0].click()#Q15
time.sleep(0)

for x in range(0,13):
    skip = driver.find_elements_by_class_name('skip')[0].click()
    time.sleep(0)
    if x==9:
        print(x)
        break


driver.find_elements_by_xpath("//*[@id='question-pg']/div[3]/div[2]/div[1]/img")[0].click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_css_selector('button[title="Copy Link"]').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_css_selector('button[title="Copy Link"]').click()
time.sleep(3)


y=webdriver.Firefox()
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
    if (y.title=='Kelab Persahabatan 2021'):
     print(y.current_url)
    
'''act=ActionChains(y)
y.find_element_by_xpath('//input[@title="Search"]').send_keys(act.key_down(Keys.CONTROL).send_keys('v').perform())'''

wait = WebDriverWait(y, 20)
element=wait.until(EC.element_to_be_clickable((By.ID,"onesignal-slidedown-cancel-button")))
element.click()
time.sleep(2)

y.find_elements_by_name('name')[0].send_keys('Deepak')
time.sleep(2)

Button=y.find_element(By.XPATH,"/html/body/div/div[2]/div[3]/div/div[4]/a")
y.execute_script('arguments[0].click()',Button)
time.sleep(2)

wait = WebDriverWait(y, 20)
#y.find_elements_by_css_selector('div[data-file-id="330"]')[0].click() #Q1
element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[data-file-id='330']")))
element.click()
time.sleep(2)



#driver.find_element_by_id('onesignal-slidedown-allow-button').click()
#time.sleep(2)



y.execute_script("window.scrollBy(0,1400)","")#auto scroll cmd
time.sleep(1)

y.find_elements_by_css_selector('div[data-file-id="338"]')[0].click() #Q2
time.sleep(3)

y.find_element(By.CSS_SELECTOR,'div[value="Berbincang dengan ibubapa"]').click()
time.sleep(2)

y.find_elements_by_css_selector('div[data-file-id="343"]')[0].click()
time.sleep(2)
y.find_element(By.CSS_SELECTOR,'div[value="35-40"]').click()
time.sleep(2)
y.find_elements_by_css_selector('div[data-file-id="322"]')[0].click()
time.sleep(2)
y.find_element(By.CSS_SELECTOR,'div[value="Menyelam"]').click()#Q7
time.sleep(2)
y.find_elements_by_css_selector('div[data-file-id="349"]')[0].click()
time.sleep(2)
y.find_element(By.CSS_SELECTOR,'div[value="Empat"]').click()
time.sleep(2)
y.find_elements_by_css_selector('div[data-file-id="356"]')[0].click()
time.sleep(2)

y.find_elements_by_css_selector('div[data-file-id="361"]')[0].click()
time.sleep(2)
y.find_elements_by_css_selector("div[value='Perjalanan masa']")[0].click()
time.sleep(2)
y.find_elements_by_css_selector('div[data-file-id="365"]')[0].click()

time.sleep(2)
y.find_elements_by_css_selector("div[value='Mei']")[0].click()
time.sleep(2)

y.find_elements_by_css_selector('div[data-file-id="382"]')[0].click()

time.sleep(2)

Button=y.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div/a[1]')
y.execute_script('arguments[0].click()',Button)
time.sleep(2)
y.quit()

Scorebord=driver.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div[3]/a')
driver.execute_script('arguments[0].click()',Scorebord)
time.sleep(4)

driver.find_element(By.XPATH,"//div[@class='top-3']/span[2]").is_selected()
time.sleep(2)

driver.find_elements_by_xpath("//a[contains(text(),'Delete')]")[0].click()
time.sleep(0)
