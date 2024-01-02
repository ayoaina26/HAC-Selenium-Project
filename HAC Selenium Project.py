from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Python27\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://eshac.humbleisd.net/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2fRegistration%2fDemographic')

search = driver.find_element_by_name('LogOnDetails.UserName')
print(search)
search.send_keys('ayoain4609')
search.send_keys(Keys.RETURN)

search = driver.find_element_by_id('LogOnDetails_Password')
search.send_keys('ayodele1')
search.send_keys(Keys.RETURN)

link = driver.find_element_by_id('hac-Classes')
link.click()

print_classwork = driver.find_element_by_id('MainContent')
print(print_classwork)


time.sleep(60)

driver.quit()
