import pytest

from pages.login_page import LoginPage
from utils.data_reader import read_csv

CASOS_LOGIN_NEGATIVO = read_csv("login_negativo.csv")


@pytest.mark.parametrize(
    "caso",
    CASOS_LOGIN_NEGATIVO,
    ids=[c["caso"] for c in CASOS_LOGIN_NEGATIVO],
)
def test_login_negativo(driver, caso):
    page = LoginPage(driver)
    page.open()
    page.login(caso["username"], caso["password"])
    assert caso["mensaje_esperado"] in page.get_error_message()
