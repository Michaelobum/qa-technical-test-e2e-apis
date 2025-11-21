import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage


def test_complete_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    confirmation_page = ConfirmationPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    inventory_page.go_to_cart()
    assert cart_page.is_cart_page()

    cart_page.go_to_checkout()

    checkout_page.fill_checkout_form(
        first_name="QA",
        last_name="Tester",
        postal_code="170123",
    )
    checkout_page.continue_to_overview()

    confirmation_page.finish_purchase()
    time.sleep(5)
    assert confirmation_page.is_order_complete()