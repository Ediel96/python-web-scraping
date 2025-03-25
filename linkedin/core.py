from selenium.webdriver import Chrome

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time #tiempo
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
import pandas as pd
import openpyxl  # Add this line

from config import LIST_JOBS, INPUT_USER, INPUT_PASSWORD, BUTTON_LOGIN, XPATH_NEXT
WAITTIME = 2

def time_sleep(wait_time=None):
    if wait_time is None:
        wait_time = WAITTIME
    time.sleep(wait_time)

def initialize_driver():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--window-size=1300,1200")
    driver = Chrome(service=service, options=option)
    return driver


def login(driver, email, password):
    driver.get("https://www.linkedin.com/login")
    time_sleep()
    driver.find_element(By.XPATH, INPUT_USER).send_keys(email)
    time_sleep()
    driver.find_element(By.XPATH, INPUT_PASSWORD).send_keys(password)
    time_sleep()
    driver.find_element(By.XPATH, BUTTON_LOGIN).click()
    time_sleep()

    print("Login successful")
    return driver

def list_job(driver):
    time_sleep(1)
    # Buscar LISTA DE TRABAJOS
    list_jobs = driver.find_element(By.XPATH, LIST_JOBS)
    # Encuentra todos los elementos 'li' dentro de la lista de trabajos
    job_items = list_jobs.find_elements(By.XPATH, '//li[contains(@id, "ember") and contains(@class, "relative scaffold-layout__list-item")]')

    jobs = []

    print(f"Found {len(job_items)} jobs")

    for job in job_items:
            elementById = job.get_attribute('id')
            print(elementById)
            job_element = Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'li#{elementById} a.job-card-container__link')))
            driver.execute_script("arguments[0].scrollIntoView();", job_element)
            url = job_element.get_attribute('href')
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'li#{elementById} div div'))).click()
            time_sleep(WAITTIME)
            #Info del trabajo
            list_info_element = Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.job-details-jobs-unified-top-card__primary-description-container div')))
            list_info = list_info_element.find_elements(By.CSS_SELECTOR, 'span')
            time = list_info[4].get_attribute('text')
            application = list_info[9].get_attribute('text')

            job_title = Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'li#{elementById} div.full-width.artdeco-entity-lockup__title'))).text
            company_name = Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'li#{elementById} div.artdeco-entity-lockup__subtitle'))).text
            location = Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'li#{elementById} ul.job-card-container__metadata-wrapper li'))).text
        # try:
        #     posting_date = job.find_element(By.CSS_SELECTOR, 'time').text
        #     print(posting_date)
        # except Exception as e:
        #     print(f"Error fetching posting date: {e}")
        #     posting_date = None

            job_info = {
                'url': url,
                'title': job_title,
                'company': company_name,
                'location': location,
                'time': time,
                'application': application
                # 'posted': posting_date
            }
            jobs.append(job_info)

    return jobs

def next_page(driver):
    time_sleep()
    # Click on the next button
    driver.find_element(By.XPATH, XPATH_NEXT).click()
    time_sleep()

def scroll_page(driver, direction="down"):
    """Scroll up or down the page"""
    scrollable_div = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div')

    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
    while True:
        if direction == "down":
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        elif direction == "up":
            driver.execute_script("arguments[0].scrollTop = 0", scrollable_div)
        else:
            raise ValueError("Direction must be 'up' or 'down'")

        time.sleep(5)

        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

        if new_height == last_height:
            break

        last_height = new_height