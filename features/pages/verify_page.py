from selenium.webdriver.common.by import By
from features.pages.base_page import Page
from time import sleep

class verify_Page(Page):

    check_1 = (By.XPATH, "//div[@class='lotion-your-h3--price size']")
    check_2 = (By.XPATH, "//div[@class='back-text']")
    check_3 = (By.XPATH, "//div[@class='next-step--']")

    def click_subscription_button(self):
        self.click(*self.subscription)
        sleep(4)

    def verify_back_button(self):
        self.verify_text('Back', *self.check_2)

    def verify_upgrade(self):
        self.verify_text('upgrade', *self.check_3)