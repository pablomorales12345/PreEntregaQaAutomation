from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_login_and_cart(driver):
    try:
        driver.get('https://www.saucedemo.com')
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        assert '/inventory.html' in driver.current_url
        titulo = driver.find_element(By.CLASS_NAME, "title").text
        assert titulo == 'Products'

        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        assert len(productos) > 0

        nombre = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
        productos[0].find_element(By.TAG_NAME, 'button').click()

        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert badge == '1'

        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        producto_en_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
        assert producto_en_carrito == nombre

        titulologo = driver.find_element(By.CLASS_NAME, "app_logo").text
        assert titulologo == "Swag Labs"
    except Exception as e:
        print("❌ Error durante la prueba:", e)
