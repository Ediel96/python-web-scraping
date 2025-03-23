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

from config import LIST_JOBS, INPUT_USER, INPUT_PASSWORD, BUTTON_LOGIN
WAITTIME = 2

def time_sleep(wait_time=None):
    if wait_time is None:
        wait_time = WAITTIME
    time.sleep(wait_time)

def initialize_driver():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
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
    job_items = list_jobs.find_elements(By.TAG_NAME, 'li')

    jobs = []

    print(len(job_items))
    for job in job_items:
        try:
            url = job.find_element(By.CSS_SELECTOR, 'a.job-card-container__link').get_attribute('href')
            print(url)
        except:
            url = None
        try:
            job_title = job.find_element(By.CSS_SELECTOR, 'div.full-width.artdeco-entity-lockup__title').text
            print(job_title)
        except:
            job_title = None
        try:
            company_name = job.find_element(By.CSS_SELECTOR, 'div.artdeco-entity-lockup__subtitle').text
            print(company_name)
        except:
            company_name = None
        try:
            location = job.find_element(By.CSS_SELECTOR, 'ul.job-card-container__metadata-wrapper li').text
            print(location)
        except:
            location = None
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
            # 'posted': posting_date
        }
        jobs.append(job_info)

    return jobs