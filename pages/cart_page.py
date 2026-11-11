from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_first_item_name(self):
        nombre = self.find(self.CART_ITEM_NAME).text
        self.log.info("Producto en el carrito: %s", nombre)
        return nombre

    def start_checkout(self):
        self.log.info("Iniciando checkout")
        self.click(self.CHECKOUT_BUTTON)
