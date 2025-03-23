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
from config import LINKEDIN_USERNAME, LINKEDIN_PASSWORD
WAITTIME = 2

from core import initialize_driver, time_sleep, list_job, login


def main():
    driver = initialize_driver()
    driver.get("https://www.linkedin.com/login")
    time_sleep(WAITTIME)
    login(driver, LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

    time_sleep(WAITTIME)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4181551510&geoId=92000000&keywords=Desarrollador%20de%20JavaScript&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true")

    time_sleep(WAITTIME)
    listJob = list_job(driver)

    # Save jobs to CSV file
    df = pd.DataFrame(listJob)
    df.to_csv('/Users/eddie/Desktop/dev/work/web-scraping/jobs.csv', index=False)

    driver.quit()



if __name__ == "__main__":
    main()