from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage(object):
	def __init__(self, driver):
		self.driver = driver

	def find_element(self, loc):
		try:
			WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print('%s页面中未找到%s元素' % (self, loc))

	def is_element_exist(self, loc):
		try:
			self.driver.find_element(*loc)
			return True
		except:
			return False

