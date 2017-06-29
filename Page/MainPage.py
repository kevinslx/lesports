from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
	personal_button = (By.ID, 'left_button')
	search_button = (By.ID, 'right_button')
	close_popup_button = (By.ID, 'close')
	ok_button = (By.ID, 'btn_ok')

	def click_personal(self):
		self.find_element(self.personal_button).click()

	def click_search(self):
		self.find_element(self.search_button).click()

	def close_popup(self):
		self.find_element(self.close_popup_button).click()

	def is_popup_exist(self):
		return self.is_element_exist(self.ok_button)
