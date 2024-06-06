from features.pages import Page

# place all pages you will be using above as well as in the class Application
class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.sign_in_page = Page(driver)
        self.verify_page = Page(driver)

# steps

# create am app, features, and page folder
# in app folder create application.py file
#