from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def fill_information(self, nombre, apellido, codigo_postal):
        self.log.info("Completando datos de envío")
        self.type_text(self.FIRST_NAME, nombre)
        self.type_text(self.LAST_NAME, apellido)
        self.type_text(self.POSTAL_CODE, codigo_postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_purchase(self):
        self.log.info("Finalizando la compra")
        self.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        mensaje = self.find(self.CONFIRMATION).text
        self.log.info("Mensaje de confirmación: %s", mensaje)
        return mensaje
