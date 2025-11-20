from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    PRODUCT_ADD_BUTTONS = {
        "Sauce Labs Backpack":      (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bike Light":    (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt":  (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie":        (By.ID, "add-to-cart-sauce-labs-onesie"),
        "Test.allTheThings() T-Shirt (Red)": (
            By.ID,
            "add-to-cart-test.allthethings()-t-shirt-(red)"
        ),
    }

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name: str):
        locator = self.PRODUCT_ADD_BUTTONS[product_name]
        self.driver.find_element(*locator).click()

    def get_cart_badge_count(self) -> int:
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
