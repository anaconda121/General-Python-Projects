import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #allows bot to type things into search field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import page

PATH = "C:\Program Files (x86)\chromedriver.exe"

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		#init all vars needed
		self.driver = webdriver.Chome(PATH)
		self.driver.get("https://www.python.org/")

	#all test methods need to start with "test" 
	def test_title(self):
		mainPage = page.MainPage()
		assert mainPage.is_title_matches() #checks if python is in web title

	def tearDown(self):
		#cleaning up
		self.driver.close()

if __name__ = "__main__":
	unittest.main() #runs all unittests