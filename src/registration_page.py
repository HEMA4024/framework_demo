from time import sleep
from selenium import webdriver
from utilities.excel_lib import read_locators
from selenium.common.exceptions import NoSuchElementException


locators_path = r"C:\Users\Win\selenium_project\framework_demo\files_data\locators.xlsx"

class RegistrationPage:

    locators = read_locators(locators_path, "registration_object")

    def __init__(self, driver):
        self.driver = driver

    def register(self, first_name,last_name,email, password):
        self.driver.find_element(*self.locators["register_link"]).click()
        self.driver.find_element(*self.locators["male_radio_button"]).click()
        self.driver.find_element(*self.locators["First name_txt"]).send_keys(first_name)
        self.driver.find_element(*self.locators["Last name_txt"]).send_keys(last_name)
        self.driver.find_element(*self.locators["Email id_txt"]).send_keys(email)
        self.driver.find_element(*self.locators["Password_txt"]).send_keys(password)
        self.driver.find_element(*self.locators["Confirm password_txt"]).send_keys(password)
        self.driver.find_element(*self.locators["Register_ button"]).click()



    def is_user_register(self):
        try:
            self.driver.find_element(*self.locators["logout_link"])
            return True

        except NoSuchElementException as error:
            # print("Invalid user")
            return False

    def logout(self):
        self.driver.find_element(*self.locators["logout_link"]).click()