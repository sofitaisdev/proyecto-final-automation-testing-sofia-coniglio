from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger(self.__class__.__name__)

    def find(self, locator):
        self.log.info("Buscando elemento %s", locator)
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.log.info("Click en %s", locator)
        self.find(locator).click()

    def type_text(self, locator, text):
        self.log.info("Escribiendo en %s", locator)
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
