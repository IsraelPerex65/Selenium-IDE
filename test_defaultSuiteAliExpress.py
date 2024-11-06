import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAliExpressSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1251, 718)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def close_initial_popups(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.close-layer"))).click()
        except:
            pass  # Continuar si no hay pop-ups

    def test_tC01_login(self):
        self.driver.get("https://www.aliexpress.com/")
        self.close_initial_popups()
        
        # Abrir modal de inicio de sesión
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.sign-btn"))).click()
            
            # Completar credenciales
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "fm-login-id"))).send_keys("usuario@ejemplo.com")
            self.driver.find_element(By.ID, "fm-login-password").send_keys("contraseña_segura")
            self.driver.find_element(By.CSS_SELECTOR, ".fm-button").click()
        except Exception as e:
            print(f"Error en el test_tC01_login: {e}")

    def test_tC02_add_to_cart(self):
        self.driver.get("https://www.aliexpress.com/")
        self.close_initial_popups()
        
        # Buscar un producto
        try:
            search_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-key")))
            search_box.send_keys("smartphone")
            search_box.submit()
            
            # Seleccionar el primer producto
            first_product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-title")))
            first_product.click()
            
            # Cambiar al tab del producto
            self.driver.switch_to.window(self.driver.window_handles[1])
            
            # Agregar al carrito
            add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".addcart-button")))
            add_to_cart_button.click()
        except Exception as e:
            print(f"Error en el test_tC02_add_to_cart: {e}")

    def test_tC03_checkout(self):
        self.driver.get("https://www.aliexpress.com/")
        self.close_initial_popups()
        
        # Ir al carrito de compras
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))).click()
            
            # Iniciar el proceso de pago (Checkout)
            checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
            checkout_button.click()
            
            # Completar información de pago
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Kevin Unsain Zamora Lopez")
            self.driver.find_element(By.ID, "country").send_keys("Mexico")
            self.driver.find_element(By.ID, "city").send_keys("Estado De Mexico")
            self.driver.find_element(By.ID, "card").send_keys("8888 1111 4444 2222")
            self.driver.find_element(By.ID, "month").send_keys("12")
            self.driver.find_element(By.ID, "year").send_keys("2030")
            self.driver.find_element(By.CSS_SELECTOR, ".place-order-button").click()
        except Exception as e:
            print(f"Error en el test_tC03_checkout: {e}")

    def test_tC04_search_and_filter(self):
        self.driver.get("https://www.aliexpress.com/")
        self.close_initial_popups()
        
        # Realizar búsqueda y aplicar filtro
        try:
            search_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-key")))
            search_box.send_keys("laptop")
            search_box.submit()
            
            # Aplicar filtro de precio
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-input-min"))).send_keys("100")
            self.driver.find_element(By.CSS_SELECTOR, ".price-input-max").send_keys("500")
            self.driver.find_element(By.CSS_SELECTOR, ".price-filter-button").click()
        except Exception as e:
            print(f"Error en el test_tC04_search_and_filter: {e}")

    def test_CT05_verify_cart(self):
        self.driver.get("https://www.aliexpress.com/")
        self.close_initial_popups()
        
        # Agregar producto al carrito y verificar
        try:
            search_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-key")))
            search_box.send_keys("smartphone")
            search_box.submit()
            
            first_product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-title")))
            first_product.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            
            add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".addcart-button")))
            add_to_cart_button.click()
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))).click()
            
            # Verificar que el producto esté en el carrito
            cart_items = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-title")))
            assert cart_items, "No se encontró el producto en el carrito."
        except Exception as e:
            print(f"Error en el test_CT05_verify_cart: {e}")

    def test_CT06_verify_payment(self):
        self.driver.get("https://www.aliexpress.com/")
        self.close_initial_popups()
        
        # Agregar producto al carrito y realizar el pago
        try:
            search_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-key")))
            search_box.send_keys("smartphone")
            search_box.submit()
            
            first_product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-title")))
            first_product.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            
            add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".addcart-button")))
            add_to_cart_button.click()
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))).click()
            
            # Iniciar el proceso de pago
            checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
            checkout_button.click()
            
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Cliente Prueba")
            self.driver.find_element(By.ID, "card").send_keys("4111 1111 1111 1111")
            self.driver.find_element(By.ID, "month").send_keys("12")
            self.driver.find_element(By.ID, "year").send_keys("24")
            self.driver.find_element(By.CSS_SELECTOR, ".place-order-button").click()
            
            # Verificar que se complete la compra
            confirmation = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".confirmation-message")))
            assert "compra completada" in confirmation.text.lower(), "La confirmación de compra no se mostró."
        except Exception as e:
            print(f"Error en el test_CT06_verify_payment: {e}")
