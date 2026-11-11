from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def iniciar_sesion(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")


def test_agregar_producto_al_carrito(driver):
    iniciar_sesion(driver)
    inventario = InventoryPage(driver)

    assert inventario.count_products() == 6
    inventario.add_backpack_to_cart()
    assert inventario.get_cart_count() == "1"

    inventario.go_to_cart()
    carrito = CartPage(driver)
    assert carrito.get_first_item_name() == "Sauce Labs Backpack"


def test_checkout_completo(driver):
    iniciar_sesion(driver)
    inventario = InventoryPage(driver)
    inventario.add_backpack_to_cart()
    inventario.go_to_cart()

    carrito = CartPage(driver)
    carrito.start_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_information("Sofia", "Coniglio", "1425")
    checkout.finish_purchase()

    assert "Thank you for your order" in checkout.get_confirmation_message()
