from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class verify_page(Page):
    search_bar_1 = (By.XPATH, "//a[@href='/subscription']")
    create_account_button = (By.XPATH, "//a[@href='#']")

    def verify_account(self):
        self.verify_text("Callvin Klein", By.XPATH, "//*[@'Full-Name']")
        self.verify_text("+1 123-456-7890", By.XPATH, "//*[@'phone2']")
        self.verify_text("caliimuscle@gmail.com", By.XPATH, "//*[@'Email-3']")
        self.verify_text("yippee123!", By.XPATH, "//*[@'field']")
        self.verify_text("www.wesellhouses.com", By.XPATH, "//*[@'Company-website']")
        self.verify_text("Investor", By.XPATH, "//option[@value='Investor']")
        self.verify_text("Seller",By.XPATH, "//option[@value='Seller']")
        self.verify_text("Egypt",By.XPATH, "//*[@id='country-select']")
        self.verify_text("2-5",By.XPATH, "//*[@id='Agents-amount-2']")


    def create_account(self):
        sleep(2)
        self.wait_until_clickable_click(*self.create_account_button)