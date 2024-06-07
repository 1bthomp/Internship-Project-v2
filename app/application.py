from pages.base_page import Page
from pages.sign_in_page import sign_in_page
from pages.verify_page import verify_page


# place all pages you will be using above as well as in the class Application
class Application:
    def __init__(self, driver):
        self.sign_in_page = sign_in_page(driver)
        self.verify_page = verify_page(driver)

# steps

# create am app, features, and page folder
# in app folder create application.py file
#
