from time import sleep
from behave import given, when, then
from selenium.webdriver.support.ui import Select

@given('Open the registration page or sign up page')
def main_page(context):
    context.driver.get('https://soft.reelly.io/sign-up')
    sleep(4)
@when('Enter some test information in the input fields')
def enter_info(context):
    context.app.sign_in_page.send_first_last_name()
    sleep(4)
    context.app.sign_in_page.send_phone()
    sleep(4)
    context.app.sign_in_page.send_username()
    sleep(4)
    context.app.sign_in_page.send_password()
    sleep(4)
    context.app.sign_in_page.send_website()
    sleep(4)
    context.app.sign_in_page.scroll_down_window()
    sleep(4)
    context.app.sign_in_page.send_dropdown()
    sleep(4)
    context.app.sign_in_page.send_dropdown_2()
    sleep(4)
    context.app.sign_in_page.select_dropdown_3()
    sleep(4)
    context.app.sign_in_page.select_dropdown_4()
    sleep(4)

@then('Verify information and create account')
def verification(context):
    #context.app.verify_page.verify_account()
    #Click create account
    context.app.verify_page.create_account()
    sleep(4)
