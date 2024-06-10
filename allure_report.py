import pytest
from selenium import webdriver
import allure

@allure.feature('Google Search')
@allure.story('Basic Search')
def test_google_search():
    driver = setup_driver()
    open_google(driver)
    search_for_allure_reporting(driver)
    verify_search_results(driver)
    teardown_driver(driver)

@allure.step("Setup WebDriver")
def setup_driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path to your ChromeDriver
    return driver

@allure.step("Open Google Homepage")
def open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

@allure.step("Search for 'Allure reporting'")
def search_for_allure_reporting(driver):
    element = driver.find_element_by_name("q")
    element.send_keys("Allure reporting")
    element.submit()

@allure.step("Verify search results contain 'Allure'")
def verify_search_results(driver):
    assert "Allure" in driver.page_source

@allure.step("Teardown WebDriver")
def teardown_driver(driver):
    driver.quit()
