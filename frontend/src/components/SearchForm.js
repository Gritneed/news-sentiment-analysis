import React, { useState } from 'react';
import axios from 'axios';

const apiClient = axios.create({
  baseURL: "http://localhost:5000",
  headers: { "Content-Type": "application/json" }
});

function SearchForm({ setLoading, setResults, setError }) {
  const [company, setCompany] = useState('');
  const [daysBack, setDaysBack] = useState(7);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!company.trim()) {
      setError('Please enter a company name');
      return;
    }

    setLoading(true);
    setError(null);
    setResults(null);

    console.log("Submitting request to API...");
    console.log("Company:", company.trim());
    console.log("Days back:", daysBack);

    try {
      const response = await apiClient.post('/api/analyze', {
        company: company.trim(),
        days_back: daysBack
      });

      console.log("API Response:", response.data);
      setResults(response.data);
    } catch (err) {
      console.error('Error analyzing sentiment:', err);
      if (err.response && err.response.data && err.response.data.message) {
        setError(err.response.data.message);
      } else {
        setError('An error occurred while analyzing sentiment. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="search-form">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="company">Company Name:</label>
          <input
            type="text"
            id="company"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            placeholder="Enter company name (e.g., Apple, Tesla, Microsoft)"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="days-back">Search articles from the past:</label>
          <select 
            id="days-back" 
            value={daysBack} 
            onChange={(e) => setDaysBack(Number(e.target.value))}
          >
            <option value={1}>1 day</option>
            <option value={3}>3 days</option>
            <option value={7}>7 days</option>
            <option value={14}>14 days</option>
            <option value={30}>30 days</option>
          </select>
        </div>

        <button type="submit" className="analyze-button">Analyze Sentiment</button>
      </form>
    </div>
  );
}

export default SearchForm;