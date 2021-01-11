#file for all attributes that we are scraping
from selenium.webdriver.common.by import By

class MainPageLocators(object):
	GO_BUTTON = (By.ID, "submit") #id of go button on python page

class SearchResultsPageLocators(object):
	pass