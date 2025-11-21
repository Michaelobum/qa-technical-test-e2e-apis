from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationPage:
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def finish_purchase(self):
        """Click en Finish para completar la compra."""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def is_order_complete(self) -> bool:
        """Verifica el mensaje de confirmación."""
        header = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )
        return "Thank you for your order!" in header.text
