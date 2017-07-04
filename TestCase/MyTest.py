import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
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

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
