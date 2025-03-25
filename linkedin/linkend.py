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
TIME = 4

from core import initialize_driver, time_sleep, list_job, login, next_page, scroll_page

def acount_list_job(driver, count):
    listJob = []
    time_sleep(TIME)
    for i in range(count):
        listJob += list_job(driver)
        time_sleep(WAITTIME)
        next_page(driver)
    return listJob


def main():
    driver = initialize_driver()
    driver.get("https://www.linkedin.com/login")
    time_sleep(WAITTIME)
    login(driver, LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

    time_sleep(WAITTIME)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4190416261&distance=25&geoId=92000000&keywords=Desarrollador%20de%20JavaScript&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

    # time_sleep(WAITTIME)
    # driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/button').click()

    time_sleep(WAITTIME)
    scroll_page(driver)

    time_sleep(WAITTIME)
    listJob = acount_list_job(driver, 1)

    # Remove empty entries from the list
    listJob = [job for job in listJob if job]
    print("Total jobs found: ", len(listJob))

    # Save jobs to CSV file
    df = pd.DataFrame(listJob)
    df.to_csv('/Users/eddie/Desktop/dev/work/web-scraping/jobs.csv', index=False)

    time_sleep(1000)

    driver.quit()



if __name__ == "__main__":
    main()