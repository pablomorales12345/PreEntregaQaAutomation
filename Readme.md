# Proyecto QA Automation - Swag Labs

## Propósito del proyecto
Este proyecto automatiza pruebas funcionales del sitio [Swag Labs](https://www.saucedemo.com), validando los flujos principales: login, inventario, carrito de compras y títulos de página. El objetivo es garantizar que las funcionalidades críticas del sitio funcionen correctamente.

## Tecnologías utilizadas
- Python 3.x
- Selenium
- ChromeDriver
- Pytest (para ejecutar pruebas y generar reportes HTML)

## Funcionalidades automatizadas
1. Abrir la página y hacer login con usuario estándar.
2. Validar que se accede correctamente a la página de inventario (`/inventory.html`).
3. Verificar título de sección y del logo.
4. Contar productos visibles en inventario.
5. Mostrar nombre y precio del primer producto.
6. Añadir el primer producto al carrito.
7. Confirmar que el badge del carrito se actualiza correctamente.
8. Verificar que el producto añadido aparece en el carrito.


