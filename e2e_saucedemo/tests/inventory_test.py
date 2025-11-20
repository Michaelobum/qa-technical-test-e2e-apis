import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_single_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    print("URL después de login:", driver.current_url)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Test.allTheThings() T-Shirt (Red)")

    cart_count = inventory_page.get_cart_badge_count()

    assert cart_count == 2, f"Se esperaban 6 productos en el carrito, pero se encontraron {cart_count}"
    time.sleep(2)