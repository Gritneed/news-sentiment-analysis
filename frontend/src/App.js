import React, { useState } from 'react';
import './App.css';
import SentimentResults from './components/SentimentResults';
import SearchForm from './components/SearchForm';
import ArticleList from './components/ArticleList';

function App() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  
  console.log("Rendering App Component");
  console.log("Loading state:", loading);
  console.log("Results state:", results);
  console.log("Error state:", error);

  return (
    <div className="App">
      <header className="App-header">
        <h1>News Sentiment Analyzer</h1>
        <p>Analyze sentiment from news articles about companies</p>
      </header>
      
      <main className="App-main">
        <SearchForm 
          setLoading={setLoading} 
          setResults={setResults} 
          setError={setError} 
        />
        
        {loading && (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Analyzing news articles...</p>
          </div>
        )}
        
        {error && (
          <div className="error-container">
            <p>{error}</p>
          </div>
        )}
        
        {results && !loading && (
          <div className="results-container">
            <SentimentResults results={results} />
            <ArticleList articles={results.articles} />
          </div>
        )}
      </main>
      
      <footer className="App-footer">
        <p>Project: Artificial Intelligence - Sentiment Analysis from News Articles</p>
      </footer>
    </div>
  );
}

export default App;