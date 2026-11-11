# Proyecto Final - Automatización de Pruebas

Trabajo final integrador del curso de Testing QA. Consiste en un framework de automatización de pruebas desarrollado en Python, que cubre pruebas de interfaz de usuario sobre el sitio SauceDemo (https://www.saucedemo.com/) mediante Selenium WebDriver, y pruebas de API sobre JSONPlaceholder (https://jsonplaceholder.typicode.com) mediante la biblioteca Requests. Las pruebas de interfaz están organizadas con el patrón Page Object Model.

## Tecnologías utilizadas

- Python
- Pytest y pytest-html
- Selenium WebDriver
- Requests
- Git y GitHub

## Estructura del proyecto

- pages/: clases de cada página (BasePage, LoginPage, InventoryPage, CartPage y CheckoutPage)
- tests/: casos de prueba de login, login con datos externos, flujo de carrito y checkout, y API
- utils/: lector de archivos CSV y configuración del logging
- data/: datos de prueba utilizados por los tests parametrizados
- conftest.py: configuración del navegador y captura de pantalla ante fallas
- pytest.ini: configuración de Pytest y del reporte HTML
- reports/: reporte, log y capturas generados en cada ejecución

## Instalación de dependencias

Requisitos previos: Python y Google Chrome.

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Ejecución de las pruebas

Para ejecutar todas las pruebas:

    pytest

Para ejecutar únicamente las pruebas de API:

    pytest tests/test_api_jsonplaceholder.py

## Interpretación de los reportes

Al finalizar la ejecución se generan los siguientes archivos en la carpeta reports/:

- report.html: reporte detallado que muestra cada test ejecutado, su estado (pasado o fallado) y su duración. En los tests fallidos se incluye la captura de pantalla.
- screenshots/: capturas de pantalla de los tests fallidos, nombradas con el nombre del test y la fecha y hora de la falla.
- test_execution.log: registro de los pasos principales de cada ejecución, útil para depurar errores.

## Resultado esperado

La suite contiene 17 tests. Pasan 16 y falla 1 de manera intencional (test_forced_failure_screenshot), cuyo propósito es verificar que la captura de pantalla se guarda y se adjunta al reporte ante una falla.

## Datos de prueba

Los casos de login negativo se leen desde data/login_negativo.csv. Para agregar un caso nuevo basta con incorporar una fila al archivo, sin modificar el código.
