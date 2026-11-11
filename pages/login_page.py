from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.log.info("Abriendo %s", self.URL)
        self.driver.get(self.URL)

    def login(self, username, password):
        self.log.info("Intentando login con usuario '%s'", username)
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        mensaje = self.find(self.ERROR_MESSAGE).text
        self.log.info("Mensaje de error obtenido: %s", mensaje)
        return mensaje
