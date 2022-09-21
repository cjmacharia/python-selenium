from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# service_obj = Service("/Users/cj/Documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.get('https://google.com')
# driver.close()
from base_class import logger;

def get_logger():
    logger.test_logging().warning('were here babe')

get_logger()
