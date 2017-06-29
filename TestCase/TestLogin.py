from Page.MainPage import MainPage
from Page.PersonalPage import PersonalPage
from Page.LoginPage import LoginPage
import unittest
from appium import webdriver


class TestLogin(unittest.TestCase):
	"""测试登录"""
	def setUp(self):
		self.desired_caps = {}
		self.desired_caps['platformName'] = 'Android'
		self.desired_caps['platformVersion'] = '7.0'
		self.desired_caps['deviceName'] = 'Huawei Mate9'
		self.desired_caps['appPackage'] = 'com.lesports.glivesports'
		self.desired_caps['appActivity'] = 'com.lesports.glivesports.main.MainActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

		self.username = '13701334231'
		self.password = 'monkeysun'

	def test_login(self):
		main_page = MainPage(self.driver)
		personal_page = PersonalPage(self.driver)
		login_page = LoginPage(self.driver)
		if main_page.is_popup_exist():
			main_page.close_popup()
			main_page.click_personal()
		main_page.click_personal()
		personal_page.click_portrait()
		login_page.send_username(self.username)
		login_page.send_password(self.password)
		login_page.click_login()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()