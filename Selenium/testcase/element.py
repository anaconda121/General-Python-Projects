from selenium import webdriver
from selenium.webdriver.common.keys import Keys #allows bot to type things into search field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePageElement(object):

	def __set__(self, obj, value):
		driver = obj.driver
		WebDriverWait(driver, 100).until(
			lambda driver: driver.find_element_by_name(self.locator)
		)
		driver.find_element_by_name(self.locator).clear()
		driver.find_element_by_name(self.locator).send_keys(value)