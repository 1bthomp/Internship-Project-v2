from time import sleep
from behave import given, when, then

@given('Open main page and login')
def main_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(4)
    # Navigate to the URL

    #Search in user
    context.app.sign_in_page.send_username()
    #search_bar_1.clear()
    #search_bar_1.send_keys("Thompb155@gmail.com")

    # Search password
    context.app.sign_in_page.send_password()
    #search_bar_2.clear()
    #search_bar_2.send_keys("@qqD9Kfkpymn5Fb")

    # Click login
    context.app.sign_in_page.click_continue()
    sleep(4)


@when('Click on settings, subscription and payment options')
def settings_subs_payment(context):
    #Click settings (uncomment if needed)
    context.app.sign_in_page.click_settings()
    sleep(4)


@then('Verify subscription, back button, and upgrade plan')
def verification(context):
    #Click subscription
    context.app.verify_page.click_subscription_button()
    context.app.verify_page.verify_back_button()
    context.app.verify_page.verify_upgrade()
