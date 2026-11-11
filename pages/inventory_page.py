from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def count_products(self):
        self.find(self.PRODUCTS)
        cantidad = len(self.driver.find_elements(*self.PRODUCTS))
        self.log.info("Productos visibles: %s", cantidad)
        return cantidad

    def add_backpack_to_cart(self):
        self.log.info("Agregando la mochila al carrito")
        self.click(self.ADD_BACKPACK_BUTTON)

    def get_cart_count(self):
        return self.find(self.CART_BADGE).text

    def go_to_cart(self):
        self.log.info("Yendo al carrito")
        self.click(self.CART_LINK)
