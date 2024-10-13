from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

# Initialize the dataset
dataset = {"Title": [], "Description": [], "Skills": []}

# Scrape the first 2 pages
for page_num in range(1, 3):  # This will scrape pages 1 to 2
    print(f"Scraping page {page_num}...")

    # Navigate to the correct URL for the current page
    driver.get(f'https://www.freelancer.com/jobs/{page_num}/')

    # Wait for the job links to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.JobSearchCard-primary-heading-link'))
    )

    # Step 1: Scrape the main page and collect job URLs
    job_elements = driver.find_elements(By.CSS_SELECTOR, 'a.JobSearchCard-primary-heading-link')
    job_urls_set = set()

    # Collect all job URLs on the page
    for job in job_elements:
        job_title = job.text
        job_url = job.get_attribute('href')
        job_urls_set.add((job_title, job_url))  # Using a set to avoid duplicates

    job_urls = list(job_urls_set)  # Convert set back to list

    # Step 2: Visit each job URL to collect the full description and skills
    for title, job_url in job_urls:
        driver.get(job_url)
        time.sleep(2)  # Wait for the page to load

        try:
            description_element = driver.find_element(By.CSS_SELECTOR, 'fl-text.Project-description')
            description = description_element.text.strip()
        except Exception as e:
            description = "No description available"
            print(f"Error occurred while fetching description for {title}: {e}")

        # Scrape skills
        try:
            skills_elements = driver.find_elements(By.CSS_SELECTOR, 'fl-tag.ng-star-inserted')
            skills = ', '.join([skill.text for skill in skills_elements])
        except Exception as e:
            skills = "No skills available"
            print(f"Error occurred while fetching skills for {title}: {e}")

        # Append to the dataset
        dataset["Title"].append(title)
        dataset["Description"].append(description)
        dataset["Skills"].append(skills)

        time.sleep(1)  # Pause between requests

    print(f"Completed scraping for page {page_num}.")

# Step 3: Save data to CSV
df = pd.DataFrame(dataset)
df.to_csv('plstestjob_data_selenium.csv', index=False)

# Close the WebDriver
driver.quit()

print("Scraping complete, data saved to job_data_selenium.csv")
