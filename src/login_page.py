import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from utilities.excel_lib import read_locators


locators_path = r"C:\Users\Win\selenium_project\framework_demo\files_data\locators.xlsx"
# class LoginPage:
#
# 	def click_login_link(self):
# 		driver.find_element("link text", "Log in").click()
#
# 	def enter_email(self):
# 		driver.find_element("id", "Email").send_keys("abc@gmail.com")
#
# 	def enter_password(self):
# 		driver.find_element("id", "Password").send_keys("abc123")
#
# 	def click_remember_me(self):
# 		driver.find_element("id", "RememberMe").click()
#
# 	def click_login_btn(self):
# 		driver.find_element("xpath", '//input[@value="Log in"]').click()


class LoginPage:

	locators = read_locators(locators_path, "login_objects")

	def __init__(self, driver):
		self.driver = driver

	def login(self, email, password):
		self.driver.find_element(*self.locators["login_link"]).click()
		self.driver.find_element(*self.locators["email_txt"]).send_keys(email)
		self.driver.find_element(*self.locators["password_txt"]).send_keys(password)
		self.driver.find_element(*self.locators["remember_checkbox"]).click()
		self.driver.find_element(*self.locators["login_btn"]).click()

	def is_user_logged_in(self):
		try:
			self.driver.find_element(*self.locators["logout_link"])
			# print("user logged in successfully")
			return True

		except NoSuchElementException as error:
			# print("Invalid user")
			return False

	def logout(self):
		self.driver.find_element(*self.locators["logout_link"]).click()
