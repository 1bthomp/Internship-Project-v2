from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class sign_in_page(Page):
    # Search in user/password
    search_bar_1 = (By.ID, "email-2")
    search_bar_2 = (By.ID, "field")
    continue_button = (By.XPATH, "//a[@href='#']")
    settings = (By.XPATH, "//a[@href='/settings']")

    def send_username(self):
        self.input_text(*self.search_bar_1, text="Thompb155@gmail.com")

    def send_password(self):
        self.input_text(*self.search_bar_2, text="@qqD9Kfkpymn5Fb")

    def click_continue(self):
        implicit_wait = WebDriverWait(self.driver, 10)
        self.wait_until_clickable_click(*self.continue_button)

    def click_settings(self):
        # self.wait_until_clickable_click(*self.settings)
        element = self.find_elements(*self.settings)
        element[2].click()
