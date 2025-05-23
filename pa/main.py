from selenium.webdriver import Chrome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time #tiempo
# from selenium.webdriver.chrome.service import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

import requests

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


        list_href = []
        list

        for i in range(2, 295):
            try:
                list_table = Wait(driver, 20).until(
                    lambda d: d.find_element(By.XPATH, "//*[@id='footable_1056']/tbody")
                )
                rows = list_table.find_elements(By.TAG_NAME, "tr")

                for row in rows:
                    try:
                        class_row = row.get_attribute("class")
                        try:
                            href = row.find_element(By.XPATH, f"//tr[contains(@class, '{class_row}')]/td/p/a").get_attribute("href")
                            # print(f"class: {class_row} href: {href}")
                            list_href.append(href)
                        except Exception as e:
                            print(f"Error al obtener el href de una fila: {e}")
                            # list_href.append(None)  # Almacenar None si no se encuentra el elemento
                        # list_href.append(href)
                    except Exception as e:
                        print(f"Error al obtener el href de una fila: {e}")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Click on the pagination button
                string = f"//a[@aria-label='next']"
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
        # with open("list_href.txt", "a") as file:
        #     for href in list_href:
        #         file.write(href + "\n")

        # download files
        for index, href in enumerate(list_href):
            try:
                response = requests.get(href)
                if response.status_code == 200:
                    with open(f"downloads/file_{index + 1}.pdf", "wb") as file:
                        file.write(response.content)
                    print(f"File {index + 1} downloaded successfully.")
                else:
                    print(f"Failed to download file {index + 1}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error downloading file {index + 1}: {e}")
        # # export to text file


        # # export to json file
        # import json
        # with open("list_href.json", "w") as file:
        #     json.dump(list_href, file, indent=4)

        # # export to csv file
        # import csv
        # with open("list_href.csv", "w", newline='') as file:
        #     writer = csv.writer(file)
        #     for href in list_href:
        #         writer.writerow([href])

    except Exception as e:
        print(f"Error general: {e}")
    finally:
        time.sleep(num_sleep)
        driver.quit()


if __name__ == "__main__":
    main()