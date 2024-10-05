# Job Scraper Tool (Frontend & Backend)

This project consists of two parts: a **React-based frontend** and a **Flask-based backend** for scraping jobs from multiple job boards (LinkedIn, Indeed, Glassdoor, and ZipRecruiter).

The project allows users to input job search parameters (keywords, location, and email), which are sent to the backend to scrape job listings and return them in a CSV file.

---

## Project Overview

- **Frontend**: Built with React, this part of the project provides a simple form where users can search for jobs.
- **Backend**: Built with Flask and integrated with the JobSpy library, this part handles job scraping based on user input, aggregates job data, and returns it as a CSV file.

---

## Setup Instructions

### Prerequisites

- **Node.js** (for the frontend)
- **Python 3.10+** (for the backend)
- **Pip** (for Python dependencies)

### 1. Clone the repository

```bash
git clone <repository-url>
cd JobSpy

2. Running the Backend
 1.Navigate to the backend directory:
 cd src

Create a Python virtual environment and activate it:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate   # Windows
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Start the Flask server:

bash
Copy code
python app.py
The backend should now be running on http://localhost:5000.

3. Running the Frontend
Navigate to the frontend directory:

bash
Copy code
cd src/job-scraper-frontend
Install frontend dependencies:

bash
Copy code
npm install
Start the React development server:

bash
Copy code
npm start
This will open the frontend on http://localhost:3000.

Integration (Frontend & Backend)
The frontend React app submits search queries to the Flask backend. The backend scrapes job postings and returns the results in a CSV file.

Make sure both servers (frontend and backend) are running simultaneously:

Frontend: http://localhost:3000
Backend: http://localhost:5000
API Endpoint
The frontend sends job search parameters to the backend using a POST request to the following endpoint:

bash
Copy code
POST /api/scrape-jobs
Example Request Body
json
Copy code
{
  "keywords": "software engineer",
  "location": "Dallas, TX",
  "email": "test@example.com"
}
The backend will scrape the job listings, save them to jobs.csv, and return a success response.

Troubleshooting
Common Issues and Fixes
Frontend shows 'An error occurred while processing your request':

Ensure that the backend Flask server is running on http://localhost:5000.
Check for CORS-related issues if the frontend can't communicate with the backend. We enabled flask-cors to resolve this issue.
Backend not found (404 error):

If you're getting 404 errors when accessing the backend on http://localhost:5000, ensure that you are correctly running the Flask server and that the /api/scrape-jobs endpoint is being hit.
ModuleNotFoundError for Flask or other packages:

Ensure that all required Python packages are installed by running pip install -r requirements.txt in the backend directory.
Rate-limiting or job board issues:

Job boards like LinkedIn and ZipRecruiter may enforce rate limits. You can handle this by using proxies or reducing the number of results requested.
Project Structure
The project is structured as follows:

graphql
Copy code
JobSpy/
├── src/
│   ├── job-scraper-frontend/  # React frontend
│   ├── jobspy/                # Job scraping library (backend logic)
│   ├── app.py                 # Flask API for scraping jobs
│   ├── run_scraper.py         # Script for manually running the scraper
│   ├── tests/                 # Unit tests
│   └── requirements.txt       # Python dependencies
├── README.md                  # Main README (this file)
Future Enhancements
Adding pagination for job results.
Improving the user interface and error handling.
Enhancing job filtering options (e.g., job type, remote jobs, salary ranges).
Contact