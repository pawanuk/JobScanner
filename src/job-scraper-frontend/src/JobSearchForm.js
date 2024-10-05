import React, { useState } from 'react';
import axios from 'axios';

const JobSearchForm = () => {
  const [keywords, setKeywords] = useState('');
  const [location, setLocation] = useState('');
  const [email, setEmail] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const searchData = { keywords, location, email };

    try {
      setIsSubmitting(true);

      // Send data to backend via correct API endpoint
      await axios.post('http://localhost:5000/api/scrape-jobs', searchData);
      // Update to the correct Flask API

      alert('Job search in progress! The CSV will be emailed to you or available for download.');
      setIsSubmitting(false);
    } catch (err) {
      console.error(err);
      alert('An error occurred while processing your request.');
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Keywords</label>
        <input 
          value={keywords}
          onChange={(e) => setKeywords(e.target.value)} 
          placeholder="e.g., Playwright, Automation"
        />
      </div>
      <div>
        <label>Location</label>
        <input 
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="e.g., London"
        />
      </div>
      <div>
        <label>Email</label>
        <input 
          type="email" 
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="e.g., your-email@example.com"
        />
      </div>
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Searching...' : 'Search Jobs'}
      </button>
    </form>
  );
};

export default JobSearchForm;
