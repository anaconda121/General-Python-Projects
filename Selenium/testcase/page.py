from locator import *

class BasePage(object):

	def __init__(self, driver):
		self.driver = driver

class MainPage(BasePage):

	def is_title_matches(self):
		return "Python" in self.driver.title

	def click_go_button(self):
		element = self.driver.find_element(*MainPageLocators.GO_BUTTON) #separates into 2 objects
		element.click()

class SearchResultPage(BasePage):

	def is_results_found(self):
		return "No results found." not in self.driver.page_source