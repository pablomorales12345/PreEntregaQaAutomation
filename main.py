from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--start-maximized')  # Ventana grande
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)  # Espera implícita profesional

try:
    # 1) Abrir la página y hacer login
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # 2) Validar que estamos en inventario
    assert '/inventory.html' in driver.current_url
    print("✅ Login Exitoso y estás en la página de inventario.")


    # 3) Verificar título de sección
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == 'Products'
    print('Título de sección OK →', titulo)

    # 4) Contar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos) > 0  # Confirma que hay al menos un producto
    print(f'Se encontraron {len(productos)} productos.')

    # Mostrar nombre y precio del primer producto
    nombre = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
    precio = productos[0].find_element(By.CLASS_NAME, 'inventory_item_price').text
    print(f'Primer producto → Nombre: {nombre}, Precio: {precio}')

    # 5) Añadir el primer producto al carrito
    productos[0].find_element(By.TAG_NAME, 'button').click()

    # 6) Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == '1'
    print('Carrito OK →', badge)
    
    # 7) Ir al carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # 8) Verificar que el producto añadido está listado en el carrito
    producto_en_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
    assert producto_en_carrito == nombre  # 'nombre' es el del primer producto
    print(f'Producto en carrito OK → {producto_en_carrito}')
    
    # Verificar el título "Swag Labs"
    titulologo = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert titulologo == "Swag Labs", f"❌ Título incorrecto. Se obtuvo: {titulologo}"
    print("✅ Título OK →", titulologo)

    time.sleep(2)
except Exception as e:
    print("❌ Error durante la prueba:", e)

finally:
    driver.quit()

