import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1251, 718)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_tC01(self):
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "sign-username"))).send_keys("Invitado")
        self.driver.find_element(By.ID, "sign-password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#signInModal .btn-primary").click()
  
    def test_tC02(self):
        self.driver.get("https://www.demoblaze.com/cart.html")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))).click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Kevin Unsain Zamora Lopez")
        self.driver.find_element(By.ID, "country").send_keys("Mexico")
        self.driver.find_element(By.ID, "city").send_keys("Estado De Mexico")
        self.driver.find_element(By.ID, "card").send_keys("8888 1111 4444 2222")
        self.driver.find_element(By.ID, "month").send_keys("12")
        self.driver.find_element(By.ID, "year").send_keys("2030")
        self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
        
        # Esperar alerta sin assert para continuar
        try:
            WebDriverWait(self.driver, 15).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass  # Continuar si la alerta no aparece

    def test_tC03(self):
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("qwertyu")
        self.driver.find_element(By.ID, "loginpassword").send_keys("qwertyy")
        self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass  # Continuar si la alerta no aparece
  
    def test_tC04(self):
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "narvbarx"))).click()
  
    def test_tC05(self):
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart_button.click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass  # Continuar si la alerta no aparece
        
        self.driver.find_element(By.ID, "cartur").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".active > .nav-link")))
        self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Iphone 6 32gb"))).click()
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
        add_to_cart_button.click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass  # Continuar si la alerta no aparece
        
        self.driver.find_element(By.ID, "cartur").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success:nth-child(2) a"))).click()
  
    def test_tC06(self):
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
        
        place_order_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success")))
        place_order_button.click()
        
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Kevin Unsain Zamora Lopez")
        self.driver.find_element(By.ID, "country").send_keys("Mexico")
        self.driver.find_element(By.ID, "city").send_keys("Estado De Mexico")
        self.driver.find_element(By.ID, "card").send_keys("8888 1111 4444 2222")
        self.driver.find_element(By.ID, "month").send_keys("12")
        self.driver.find_element(By.ID, "year").send_keys("2030")
        self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
        
        try:
            WebDriverWait(self.driver, 15).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass  # Continuar si la alerta no aparece
