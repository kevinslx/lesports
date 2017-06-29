from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class PersonalPage(BasePage):
	portrait = (By.ID, 'personal_ic_portrait')

	def click_portrait(self):
		self.find_element(self.portrait).click()