from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"
from time import sleep
from behave import given, when, then
# Get the path to the ChromeDriver executable
# Set Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
# Create a new Chrome browser instance
def browser_init(context):
    """
    param context: Behave context
    """
    context.driver_path = ChromeDriverManager().install()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    service = Service(context.driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###


#service = Service(executable_path='/Users/svetlanalevinsohn/careerist/18-python-selenium-automation/geckodriver')
#context.driver = webdriver.Firefox(service=service)

### HEADLESS MODE ####
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#service = Service(ChromeDriverManager().install())
#context.driver = webdriver.Chrome(
 #   options=options,
  #  service=service
#)

def before_all(context):
    # Get the path to the ChromeDriver executable

    context.driver = get_driver(context.config.driver)
    context.URL = context.config.URL
    driver = webdriver.Chrome(executable_path = '/Users/svetlanalevinsohn/careerist/18-python-selenium-automation/geckodriver')
    driver_path = ChromeDriverManager().install()

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # create a new Chrome browser instance
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
def after_all(context):
    context.driver.quit()


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass

