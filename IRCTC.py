from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

chromeb= webdriver.Chrome(executable_path=r"C:\Users\TOSHIBA\Downloads\chromedriver_win32 (2)\chromedriver.exe")
chromeb.get("https://www.irctc.co.in/nget/train-search")

button1= chromeb.find_element_by_xpath("//button[@class='btn btn-primary']")
button1.click()

login1=chromeb.find_element_by_class_name("h_menu_drop_button")
login1.click()

login1=chromeb.find_element_by_xpath("//*[@id='slide-menu']/p-sidebar/div/nav/div/label/button")
login1.click()
login1=chromeb.find_element_by_name("userId")
login1.send_keys("dhana_rai")
time.sleep(1)

login1=chromeb.find_element_by_name("pwd")
login1.send_keys("prithvi501")
time.sleep(15)

login1=chromeb.find_element_by_xpath("//*[@id='login_header_disable']/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button")
login1.click()
input1= chromeb.find_element_by_xpath("//*[@id='origin']/span/input")
input1.send_keys("MUMBAI CENTRAL - BCT")
input2= chromeb.find_element_by_xpath("//*[@id='destination']/span/input")
input2.send_keys("UDUPI - UD")
time.sleep(2)

Class = chromeb.find_element_by_xpath('//*[@id="journeyClass"]/div/div[3]')
Class.click()
Class = chromeb.find_element_by_xpath('//*[@id="journeyClass"]/div/div[4]/div/ul/li[7]')
Class.click()

Find_train = chromeb.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button')
Find_train.click()

time.sleep(5)
next_date = chromeb.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/div[3]/a')
next_date.click()

time.sleep(2)
tatkal = chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/p-dropdown/div/div[3]/span')
tatkal.click()

tatkal = chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/p-dropdown/div/div[4]/div/ul/li[5]')
tatkal.click()

check = chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[2]/div/div')
check.click()
time.sleep(2)

booknow =chromeb.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div[3]/p-panel/div/div[2]/div/div/div/table/tbody/tr/td/div/div[3]/button')
booknow.click()
time.sleep(6)

input1= chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[1]/div/div[2]/app-passenger/div/div[1]/div[1]/input')
input1.send_keys("PRITHVI SHETTY")

input1= chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[1]/div/div[2]/app-passenger/div/div[1]/div[2]/input')
input1.send_keys("21")

event = chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select')
event.click()

event = chromeb.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select/option[4]')
event.click()

#mySelect = Select(WebDriverWait(chromeb, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='journeyClass']/div/div[4]/div/ul/li[2]/span']"))))
#mySelect.select_by_value('Sleeper (SL)')
#drop_down= Select(chromeb.find_element_by_css_selector("select.ng-tns-c11-6"))
#drop_down..select_by_visible_text('Sleeper (SL)')
#drop_down.select_by_index(3)    #index of dropdown
#drop_down.select_by_value('')   #value attribute html
#print(len(drop_down.options))
#opt=drop_down.options
#print(opt[3])

time.sleep(5)

