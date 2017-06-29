from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
	usr = (By.ID, 'account_edittext')
	pwd = (By.ID, 'password_edittext')
	login_button = (By.ID, 'login_button')

	def send_username(self, username):
		self.find_element(self.usr).send_keys(username)

	def send_password(self, password):
		self.find_element(self.pwd).send_keys(password)

	def click_login(self):
		self.find_element(self.login_button).click()
