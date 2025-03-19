from selenium.webdriver import Chrome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time #tiempo
# from selenium.webdriver.chrome.service import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

#variables
USSERNAME = "standard_user"
PASSWORD = "secret_sauce"

def main():
    service=Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")

    #iniciar sesion
    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys(USSERNAME)

    pass_input =driver.find_element(By.ID, "password")
    pass_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    #agregar al carrito
    # add_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    button_1 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')

    time.sleep(5)
    driver.quit()



if __name__ == "__main__":
    main()