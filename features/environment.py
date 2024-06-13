from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    #service = Service(executable_path='/Users/svetlanalevinsohn/careerist/18-python-selenium-automation/geckodriver')
    #context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #bs_user = 'brianthompson_QjCRxc'
    #bs_key = 'syDNvJAqWUVmUcXs2bWm'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options: Options = Options()
    # bstack_options = {
    #     'os':'Android',
    #     'osVersion': '13.0',
    #     'browserName': 'Chrome',
    #     'browserVersion': '120.0',
    #     'deviceName': 'samsung galaxy s22',
    #     'deviceOrientation': 'portrait',
    #     'sessionName': 'Internship_Test_Case'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    #context.driver.maximize_window()

    # context.driver.maximize_window()
    # context.driver.set_window_size(400, 726)
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
