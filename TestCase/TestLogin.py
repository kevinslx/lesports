from Page.MainPage import MainPage
from Page.PersonalPage import PersonalPage
from Page.LoginPage import LoginPage
import unittest
from appium import webdriver
from TestCase import MyTest


class TestLogin(MyTest.MyTestCase):
	"""测试登录"""
	def test_login(self):
		main_page = MainPage(self.driver)
		personal_page = PersonalPage(self.driver)
		login_page = LoginPage(self.driver)
		if main_page.is_popup_exist():
			main_page.close_popup()
			main_page.click_personal()
		main_page.click_personal()
		personal_page.click_portrait()
		if login_page.is_current_account_exist():
			login_page.login_with_current_account()
		else:
			login_page.send_username(self.username)
			login_page.send_password(self.password)
			login_page.click_login()

if __name__ == '__main__':
	unittest.main()