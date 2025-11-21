from selenium.webdriver.common.by import By


class CartPage:
    CART_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def is_cart_page(self) -> bool:
        """Verifica que estamos en la página del carrito"""
        return "cart.html" in self.driver.current_url

    def go_to_checkout(self):
        """Click en el botón Checkout"""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
