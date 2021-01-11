from selenium import webdriver
from selenium.webdriver.common.keys import Keys #allows bot to type things into search field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) #using chrome browser

#actionchains - more advanced actions (doubleclick, etc)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5) #waits 5 seconds for page to load before executing below code

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice0"), driver.find_element_by_id("productPrice1")]

'''
items = [driver.find_element_by_id("productPrice9"), driver.find_element_by_id("productPrice8"), driver.find_element_by_id("productPrice7"), 
driver.find_element_by_id("productPrice6"), driver.find_element_by_id("productPrice5"), driver.find_element_by_id("productPrice4"),
driver.find_element_by_id("productPrice3"), driver.find_element_by_id("productPrice2"), driver.find_element_by_id("productPrice1")]
'''

actions = ActionChains(driver)
actions.click(cookie)

#pressing cookie
for i in range(5000):
	actions.perform()
	count = cookie_count.text.split(" ")[0] #grabbing only number of cookies
	
	for item in items:
		value = int(item.text)
		print(value)
		if value <= int(count):
			upgrade = ActionChains(driver)
			upgrade.move_to_element(item)
			upgrade.click()
			upgrade.perform()
