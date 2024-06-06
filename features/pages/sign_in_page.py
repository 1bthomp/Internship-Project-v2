from selenium.webdriver.common.by import By
from features.pages.base_page import Page
from time import sleep


class sign_in_page(Page):
    # Search in user/password
    search_bar_1 = (By.ID, "email-2")
    search_bar_2 = (By.ID, "field")
    continue_button = (By.LINK_TEXT, 'Continue')
    settings = (By.LINK_TEXT, 'Settings')


def send_username(self, search_bar_1):
    self.search_bar1(*self.search_bar1)


def send_password(self, search_bar_2):
    self.search_bar_2(*self.search_bar_2)


def click_continue(self):
    self.click(*self.continue_button)
    sleep(4)


def click_settings(self):
    self.click(*self.settings_button)
    sleep(4)
