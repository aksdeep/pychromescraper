import time

from webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.keys import Keys


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url('https://www.reddit.com/r/wallstreetbets/search/?q=flair%3A%22Daily%20Discussion%22&restrict_sr=1&sort=new')
    example_text = driver.get_elements_by_class_name("_eYtD2XCVieq6emjKBH3m")

    for a in example_text:
    	data = a.text

    driver.close()
    return data
