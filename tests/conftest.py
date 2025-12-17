import pytest
from src.config.drivers_factory import create_driver
from src.pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.login("cristian@crisoft.dev", "123")
    return driver