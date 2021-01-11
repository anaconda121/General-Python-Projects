from selenium import webdriver
from selenium.webdriver.common.keys import Keys #allows bot to type things into search field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) #using chrome browser

driver.get("https://techwithtim.net")
print(driver.title)

#page navigation
link = driver.find_element_by_link_text("Python Programming") #finds python programming header on side
link.click() #clicks on python programming

try:
	#wait max 10 seconds until page is loaded
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.clear() #clears query so previous text doesnt affect search
    element.click()

    get_started = WebDriverWait(driver, 10).until(
    	EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    get_started.click()

    #going back to homepage
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()

except:
    driver.quit()