from appium import webdriver

desired_caps = {}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element().se