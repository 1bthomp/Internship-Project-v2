from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class verify_page(Page):
    check_1 = (By.XPATH, "//a[@href='/subscription']")
    check_2 = (By.XPATH, "//div[@class='back-text']")
    check_3 = (By.XPATH, "//div[@class='next-step--']")

    def click_subscription_button(self):
        self.scroll_down()
        self.click(*self.check_1)
        sleep(4)

    def verify_back_button(self):
        self.verify_text('Back', *self.check_2)

    def verify_upgrade(self):
        self.verify_text('Upgrade plan', *self.check_3)
