from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
	usr = (By.ID, 'account_edittext')
	pwd = (By.ID, 'password_edittext')
	login_button = (By.ID, 'login_button')
	existing_button = (By.ID, 'button_item_showaccount')

	def send_username(self, username):
		self.find_element(self.usr).send_keys(username)

	def send_password(self, password):
		self.find_element(self.pwd).send_keys(password)

	def click_login(self):
		self.find_element(self.login_button).click()

	def login_with_current_account(self):
		self.find_element(self.existing_button).click()

	def is_current_account_exist(self):
		return self.is_element_exist(self.existing_button)
