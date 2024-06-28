from selenium.webdriver.common import by
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
import behave
from time import sleep

class sign_in_page(Page):
    # Search in user/password
    search_bar_1 = (By.ID, "Full-Name")
    search_bar_2 = (By.ID, "phone2")
    search_bar_3 = (By.ID, "Email-3")
    search_bar_4 = (By.ID, "field")
    search_bar_5 = (By.ID, "Company-website")
    dropdown_1 = (By.ID, "Role")
    dropdown_1_option = (By.XPATH, "//option[@value='Investor']")
    dropdown_2 = (By.ID, "Position")
    dropdown_2_option = (By.XPATH, "//option[@value='Manager / Director']")
    dropdown_3 = (By.ID, "country-select")
    dropdown_3_option = (By.XPATH, "//option[@value='Egypt']")
    dropdown_4 = (By.ID, "Agents-amount-2")
    dropdown_4_option = (By.XPATH, "//option[@value='2-5']")

    def send_first_last_name(self):
        self.input_text(*self.search_bar_1, text="Callvin Klein")

    def send_phone(self):
        self.input_text(*self.search_bar_2, text="+1 123-456-7890")

    def send_username(self):
        self.input_text(*self.search_bar_3, text="caliimuscle@gmail.com")

    def send_password(self):
        self.input_text(*self.search_bar_4, text="yippee123!")

    def send_website(self):
        self.input_text(*self.search_bar_5, text="www.wesellhouses.com")

    def scroll_down_window(self):
        self.scroll_down()

    def send_dropdown(self):
        #self.click(self.dropdown_1)
        #self.select_element_drop_down(text=self.dropdown_1_option)

        # Wait until dropdown is visible and interactable
        ##dropdown_1_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_1))
        # Create a Select object
        ##drop = Select(dropdown_1_element)
        # Select by visible text, value, or index
        #drop.select_by_visible_text('Investor')
        ##drop.select_by_index(1)

        #drop = Select(self.dropdown_1)
        #sleep(4)
        #drop.select_by_index(1)

        self.wait_until_clickable_click(By.XPATH, "//*[@id='Role']")
        self.select_by_visible_value("//*[@value='Investor']")

    def send_dropdown_2(self):
        self.wait_until_clickable_click(By.XPATH, "//*[@id='Position']")
        self.select_by_visible_value("//*[@value='Seller']")

        #self.click(self.dropdown_2)
        #self.click(self.dropdown_2_option)

    def select_dropdown_3(self):
        self.wait_until_clickable_click(By.XPATH, "//*[@id='country-select']")
        self.select_by_visible_value("//*[@value='Egypt']")

        #self.click(self.dropdown_3)
        #self.click(self.dropdown_3_option)

    def select_dropdown_4(self):
        self.wait_until_clickable_click(By.XPATH, "//*[@id='Agents-amount-2']")
        self.select_by_visible_value("//*[@value='2-5']")

        #self.click(self.dropdown_4)
        #self.click(self.dropdown_4_option)
