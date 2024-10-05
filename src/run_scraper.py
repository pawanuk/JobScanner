import csv
import json
import os
from jobspy import scrape_jobs

def load_search_data(input_file="search_input.json"):
    """
    Loads the search input data from a JSON file. 
    If the file doesn't exist, it returns default search data.
    """
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found! Using default search parameters.")
        return {
            "keywords": "Playwright automation tester",
            "location": "London, UK",
            "email": ""
        }

    with open(input_file, 'r') as f:
        try:
            search_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error reading '{input_file}', using default search parameters.")
            search_data = {
                "keywords": "Playwright automation tester",
                "location": "London, UK",
                "email": ""
            }

    return search_data

def scrape_and_save_jobs(search_data):
    """
    Scrapes job listings based on the provided search data and saves the results to a CSV file.
    """
    keywords = search_data.get("keywords", "Playwright automation tester")
    location = search_data.get("location", "London, UK")
    email = search_data.get("email", "")

    print(f"Scraping jobs for keywords: {keywords}, location: {location}")
    
    # Scrape jobs based on the input
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term=keywords,
        location=location,
        results_wanted=20,
        hours_old=72,  # Fetch jobs posted in the last 72 hours
        country_indeed='UK',  # Only needed for Indeed/Glassdoor
    )

    if len(jobs) == 0:
        print("No jobs found.")
        return
    
    print(f"Found {len(jobs)} jobs.")
    
    # Save the job listings to a CSV file
    csv_file = "jobs.csv"
    jobs.to_csv(csv_file, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    
    print(f"Jobs saved to {csv_file}")
    # In future, logic to email the CSV to the user can be implemented here.

def run_scraper():
    """
    Main function to run the job scraper.
    It loads search input data, scrapes the jobs, and saves the results to a CSV file.
    """
    search_data = load_search_data()
    scrape_and_save_jobs(search_data)

if __name__ == "__main__":
    run_scraper()
