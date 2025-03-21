# LinkedIn Job Scraper

This project is a web scraper that extracts job listings from LinkedIn and saves them to a CSV file.

## Description

The script uses Selenium to navigate LinkedIn job listings, extract job details, and save them to a CSV file for further analysis.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/linkedin-job-scraper.git
    cd linkedin-job-scraper
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install the ChromeDriver:
    ```sh
    webdriver-manager chrome
    ```

## Usage

1. Update the `config.py` file with the appropriate XPaths for the close button and job list:
    ```python
    CLOSE_MODEL = 'your_xpath_here'
    LIST_JOBS = 'your_xpath_here'
    ```

2. Run the script:
    ```sh
    python linkend.py
    ```

3. The job listings will be saved to `jobs.csv` in the project directory.

## Configuration

Make sure to update the `config.py` file with the correct XPaths for the close button and job list elements.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
