# Web Scraping Freelancer.com using Selenium

This project demonstrates how to scrape job listings from [Freelancer.com](https://www.freelancer.com/) using **Selenium**, a powerful web automation tool. The scraper gathers job titles, descriptions, and other relevant details from Freelancer job postings.

## Features
- Scrapes job listings from Freelancer.com.
- Extracts details such as:
  - Job title
  - Job Description
  - Skills required
- Saves the scraped data to a file (e.g., CSV, JSON).

## Requirements

To run this project, you will need to install the following dependencies:

- **Python 3.x**: Ensure that Python is installed on your system.
- **Selenium**: A Python library for browser automation.
  - Install it via pip:
    ```bash
    pip install selenium
    ```
- **Web Driver**: Selenium requires a web driver to interact with the browser.
  - For Chrome: Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your project directory or add it to your system's PATH.
  - For Firefox: Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases) if you are using Firefox.

## Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Nashhz/webscrape-selenium-freelancer.com.git
   cd webscrape-selenium-freelancer.com
   ```

2. **Install dependencies**:
   Make sure you have Selenium installed using pip:
   ```bash
   pip install selenium
   ```

3. **Download and set up the WebDriver**:
   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
   - Place the WebDriver in your project folder or ensure it's in your system's PATH.

4. **Run the web scraper**:
   You can now run the scraper script. This example assumes the script is named `freelancer_scraper.py`:
   ```bash
   python freelancer_scraper.py
   ```

## Usage

### Example Code Snippet (Basic Scraper)
```python
from selenium import webdriver

# Set up the web driver (ensure you have downloaded the appropriate driver)
driver = webdriver.Chrome()  # or webdriver.Firefox()

# Open Freelancer.com
driver.get('https://www.freelancer.com/jobs/')

# Example: Scrape job titles
jobs = driver.find_elements_by_class_name('JobSearchCard-primary-heading-link')

for job in jobs:
    print(job.text)

# Close the driver when done
driver.quit()
```

### Modify to Scrape More Data
You can modify the script to scrape additional details like the job description, budget, and skills.

## Output
The scraped data can be saved to a CSV or JSON file for further analysis. Here's an example of saving job data to a CSV file:

```python
import csv

# Assuming you have scraped the data into a list of dictionaries
jobs_data = [
    {"Title": "Job 1", "Budget": "$500", "Description": "Example description"},
    {"Title": "Job 2", "Budget": "$300", "Description": "Another example"}
]

# Save to CSV
with open('freelancer_jobs.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Budget", "Description"])
    writer.writeheader()
    writer.writerows(jobs_data)
```

## License
This project is licensed under the MIT License. Feel free to modify and use it as per your needs.

## Disclaimer
Scraping websites may violate their terms of service, and frequent requests may get your IP blocked. Be sure to check Freelancer.com's policy before scraping and use the scraper responsibly.

---
