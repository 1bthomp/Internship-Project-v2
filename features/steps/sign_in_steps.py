from time import sleep
from behave import given, when, then

@given('Open main page and login')
def main_page(context):
    # Navigate to the URL
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(4)

    #Search in user
    context.app.sign_in_page.send_username("Thompb155@gmail.com")
    #search_bar_1.clear()
    #search_bar_1.send_keys("Thompb155@gmail.com")

    # Search password
    context.app.sign_in_page.send_password("@qqD9Kfkpymn5Fb")
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
    check_1 = context.app.verify_page.click_subscription_button()
    sleep(4)

    if check_1 == "Subscription & payments":
        print("1st check passed")
    else:
        print("not verified")

    check_2 = context.app.verify_page.verify_back_button()

    if check_2 == "Back":
        print("2nd check passed")
    else:
        print("not verified")

    check_3 = context.app.verify_page.verify_upgrade()

    if check_3 == "Upgrade plan":
        print("3rd check passed")
    else:
        print("not verified")

    context.driver.quit()
