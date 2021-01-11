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

search = driver.find_element_by_name("s") #getting id of search bar
search.send_keys("test") #typing test into search bar
search.send_keys(Keys.RETURN) #clicking enter to render results

#print(driver.page_source) #gives entire source code for scraped site

#explicit wait - makes sure correct page has loaded before element is searched for to prevent exception
try:
	#wait max 10 seconds until page is loaded
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article") #finding all elements with article tag
    for article in articles:
    	header = article.find_element_by_class_name("entry-summary") #finding text of all entry-summary class in article tags
    	print(header.text)

finally:
    driver.quit()
