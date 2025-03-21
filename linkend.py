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

# Import variables from config.py
from config import CLOSE_MODEL, LIST_JOBS

def main():
    service=Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)


    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4181551510&geoId=92000000&keywords=Desarrollador%20de%20JavaScript&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true")

    # Cerrar el modal
    wait = Wait(driver, 10)
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, CLOSE_MODEL)))
    close_button.click()

    # Buscar LISTA DE TRABAJOS
    list_jobs = driver.find_element(By.XPATH, LIST_JOBS)
    job_items = list_jobs.find_elements(By.TAG_NAME, 'li')

    jobs = []
    for job in job_items:
        url = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
        job_title = job.find_element(By.CLASS_NAME, 'base-search-card__title').text
        company_name = job.find_element(By.CLASS_NAME, 'base-search-card__subtitle').text
        location = job.find_element(By.CLASS_NAME, 'job-search-card__location').text
        posting_date = job.find_element(By.TAG_NAME, 'time').text

        job_info = {
            'url': url,
            'title': job_title,
            'company': company_name,
            'location': location,
            'posted': posting_date
        }
        jobs.append(job_info)

    # Save jobs to CSV file
    df = pd.DataFrame(jobs)
    df.to_csv('/Users/eddie/Desktop/dev/work/web-scraping/jobs.csv', index=False)

    print(jobs)


    time.sleep(1000)
    driver.quit()



if __name__ == "__main__":
    main()