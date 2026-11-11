import base64
import os
from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"reports/screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(filename)

            # Adjunta la captura dentro del reporte HTML
            with open(filename, "rb") as archivo:
                imagen = base64.b64encode(archivo.read()).decode("utf-8")
            rep.extras = getattr(rep, "extras", []) + [extras.image(imagen)]
