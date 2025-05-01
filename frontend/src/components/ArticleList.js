import React from 'react';

function ArticleList({ articles = [] }) {
  if (!articles || articles.length === 0) {
    return <p>No articles found</p>;
  }

  return (
    <div className="article-list">
      <h2>Articles Analyzed</h2>
      <p>Total articles: {articles.length}</p>
      
      <div className="articles-container">
        {articles.map((article, index) => (
          <div key={index} className="article-card">
            <h3>{article.title}</h3>
            <p className="article-source">{article.source}</p>
            <p className="article-date">{new Date(article.published_at).toLocaleDateString()}</p>
            <p className="article-sentiment">
              Sentiment: 
              <span className={`sentiment-${article.sentiment.toLowerCase()}`}>
                {article.sentiment}
              </span>
            </p>
            {article.url && (
              <a href={article.url} target="_blank" rel="noopener noreferrer" className="article-link">
                Read Article
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default ArticleList;