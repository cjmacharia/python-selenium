import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageobjects.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# request is a default instance for fixture
@pytest.fixture
def init_driver(request):
    browser_name = request.config.getoption("browser_name")
    service_obj = None
    if browser_name == "firefox":
        service_obj = Service(os.path.join(os.getcwd(), 'drivers/geckodriver'))
    else:
        service_obj = Service(os.path.join(os.getcwd(), 'drivers/chromedriver'))
    driver = webdriver.Chrome(service=service_obj)
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.close()


@pytest.fixture(params=[{'email': "standard_user", 'password': "secret_sauce"}])
def standard_login(init_driver, request):
    login_page = LoginPage(init_driver)
    login_page.enter_email(request.param['email'])
    login_page.enter_password(request.param['password'])
    login_page.click_login()
    yield login_page
