import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from urls import *
from data import Credentials
from locators import Locators

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    service = Service("/Users/diananigma/Downloads/WebDriver/bin/chromedriver")
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(Curls.main_site)
    yield browser
    browser.quit()


@pytest.fixture()
def login(driver):
    driver.get(Curls.auth_endpoint)
    driver.find_element(*Locators.NAME).send_keys(Credentials.name)
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.REG_BUTTON).click()










