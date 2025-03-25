from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Import variables from environment
LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

#XPATHS
INPUT_USER = "//input[@id='username']"
INPUT_PASSWORD = "//input[@id='password']"
BUTTON_LOGIN = "//button[@type='submit']"

CLOSE_MODEL = '//*[@id="base-contextual-sign-in-modal"]/div/section/button'
LIST_JOBS = '//*[@id="main"]/div/div[2]/div[1]/div/ul'

XPATH_NEXT = '//button[contains(@class, "artdeco-button--muted") and contains(@class, "jobs-search-pagination__button--next")]'