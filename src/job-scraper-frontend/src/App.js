import React from 'react';
import JobSearchForm from './JobSearchForm';  // Import the form component
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Job Scraper Tool</h1>
        <p>Enter keywords and location to find relevant jobs. Results will be emailed to you.</p>
        
        {/* Render the Job Search Form */}
        <JobSearchForm />
      </header>
    </div>
  );
}

export default App;
