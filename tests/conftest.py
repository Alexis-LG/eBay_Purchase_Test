import pytest
from chromedriver_binary.utils import get_chromedriver_filename
from selenium.webdriver.chrome.webdriver import WebDriver

from Page.HomePage import HomePage


@pytest.fixture
def browser():
    with WebDriver(get_chromedriver_filename()) as browser:
        browser.maximize_window()
        browser.get("https://www.ebay.com")
        yield browser


@pytest.fixture()
def homepage(browser):
    return HomePage(browser)
