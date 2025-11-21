from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """Rellena el formulario de checkout (Step One)."""
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        )

        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

        self.driver.find_element(*self.POSTAL_CODE_INPUT).clear()
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continue_to_overview(self):
        """Hace clic en Continue para pasar al overview (Step Two)."""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
