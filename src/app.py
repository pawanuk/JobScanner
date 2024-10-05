from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
import csv
import json
import os
from jobspy import scrape_jobs

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app

# Root route to handle the base URL
@app.route("/")
def home():
    return "Job Scraper Backend is Running"
@app.route("/api/scrape-jobs", methods=["POST"])
def scrape_jobs_endpoint():
    try:
        search_data = request.json
        if not search_data:
            return jsonify({"error": "No search data provided"}), 400

        keywords = search_data.get("keywords", "Playwright automation tester")
        location = search_data.get("location", "London, UK")
        email = search_data.get("email", "")

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
            return jsonify({"error": "No jobs found"}), 404

        # Save the job listings to a CSV file
        csv_file = "jobs.csv"
        jobs.to_csv(csv_file, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
        
        return jsonify({"message": "Jobs scraped successfully", "csv": csv_file}), 200

    except Exception as e:
        # Print the error for debugging purposes
        print(f"Error during scraping: {e}")
        return jsonify({"error": "Failed to scrape jobs"}), 500

if __name__ == "__main__":
    app.run(debug=True)
