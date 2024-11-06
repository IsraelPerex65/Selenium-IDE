from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time

# Configuración inicial
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # Paso 1: Navegar a la página principal de demoblaze
    driver.get("https://www.demoblaze.com/")
    
    # Paso 2: Navegar a la categoría "Phvenones"
    phones_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
    phones_link.click()

    # Paso 3: Seleccionar el producto "Samsung galaxy s6"
    samsung_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
    samsung_link.click()

    # Paso 4: Validar el nombre y el precio del producto
    product_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.name"))).text
    product_price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.price-container"))).text

    assert product_name == "Samsung galaxy s6", f"Error: El nombre del producto es {product_name}."
    assert "$360" in product_price, f"Error: El precio del producto es {product_price}."

    # Paso 5: Agregar al carrito
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))
    add_to_cart_button.click()
    
    # Esperar y aceptar la alerta si está presente
    try:
        wait.until(EC.alert_is_present())  # Espera hasta que la alerta esté presente
        Alert(driver).accept()
    except NoAlertPresentException:
        print("No se encontró ninguna alerta después de hacer clic en 'Add to cart'.")

    # Paso 6: Ir al carrito
    cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cart")))
    cart_link.click()

    # Paso 7: Validar el producto en el carrito
    cart_product_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(2)"))).text
    cart_product_price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(3)"))).text

    assert cart_product_name == "Samsung galaxy s6", f"Error: El nombre del producto en el carrito es {cart_product_name}."
    assert cart_product_price == "360", f"Error: El precio del producto en el carrito es {cart_product_price}."

    # Paso 8: Proceder a la compra
    place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
    place_order_button.click()

    # Paso 9: Completar la información de compra
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    credit_card_input = driver.find_element(By.ID, "card")
    name_input.send_keys("Test User")
    credit_card_input.send_keys("1234567890123456")

    # Paso 10: Simular el pago
    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Purchase']")))
    purchase_button.click()

    # Paso 11: Verificar confirmación de compra
    confirmation_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2"))).text
    assert confirmation_message == "Thank you for your purchase!", "Error: No se encontró el mensaje de confirmación."

    print("Test completado exitosamente.")

finally:
    # Cerrar el navegador
    time.sleep(3)
    driver.quit()
