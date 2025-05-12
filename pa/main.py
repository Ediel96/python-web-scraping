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
num_sleep = 1

def main():
    try:
        service = Service(ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_argument("--window-size=1920,1080")
        driver = Chrome(service=service, options=option)
        driver.get("https://courdappelcommerceabidjan.org/arrets-de-la-cour-dappel-de-commerce-dabidjan/")

        time.sleep(num_sleep)

        list_href = []

        for i in range(2, 99):
            try:
                list_table = Wait(driver, 20).until(
                    lambda d: d.find_element(By.XPATH, "//*[@id='footable_1056']/tbody")
                )
                rows = list_table.find_elements(By.TAG_NAME, "tr")

                for row in rows:
                    try:
                        class_row = row.get_attribute("class")
                        href = row.find_element(By.XPATH, f"//tr[contains(@class, '{class_row}')]/td/p/a").get_attribute("href")
                        list_href.append(href)
                    except Exception as e:
                        print(f"Error al obtener el href de una fila: {e}")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(num_sleep)
                # Click on the pagination button
                string = f"//a[@aria-label='page {i}']"
                pagination_button = Wait(driver, 20).until(
                    lambda d: d.find_element(By.XPATH, string)
                )
                if pagination_button:
                    pagination_button.click()
                    print(f"pages {i} clicked.")
                else:
                    print(f"Pagination button with XPath {string} not found.")
                time.sleep(num_sleep)
            except Exception as e:
                print(f"Error en la iteración {i}: {e}")

        print("Total href:", len(list_href))  # Print the total number of hrefs
        # export to text file
        with open("list_href.txt", "w") as file:
            for href in list_href:
                file.write(href + "\n")

    except Exception as e:
        print(f"Error general: {e}")
    finally:
        time.sleep(num_sleep)
        driver.quit()


if __name__ == "__main__":
    main()