from pages.login_page import LoginPage


def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_locked_out_user(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "Epic sadface" in page.get_error_message()


def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    assert "Epic sadface" in page.get_error_message()


def test_empty_credentials(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert "Username is required" in page.get_error_message()


def test_forced_failure_screenshot(driver):
    page = LoginPage(driver)
    page.open()
    assert "wrong_url_intentionally" in driver.current_url
