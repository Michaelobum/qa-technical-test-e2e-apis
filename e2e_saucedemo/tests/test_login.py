import pytest
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

def test_login_invalid(driver):
    page = LoginPage(driver)
    page.open()
    page.login("bad_user", "bad_password")

    error = page.get_error()
    assert "Username and password do not match" in error
