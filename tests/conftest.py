import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# request is a default instance for fixture
@pytest.fixture(scope="class")
def setUp(request):
    browser_name = request.config.getoption("browser_name")
    service_obj = None
    if browser_name == "firefox":
        service_obj = Service("/Users/cj/Documents/geckodriver")
    else:
        service_obj = Service("/Users/cj/Documents/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    request.cls.driver = driver
    yield
    driver.close()
