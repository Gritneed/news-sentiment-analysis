import React from 'react';

function SentimentResults({ results = {} }) {
  if (!results.sentiment_counts) {
      return <p>No data available</p>;
  }

  return (
      <div>
          <p>Positive: {results.sentiment_counts.positive}</p>
          <p>Negative: {results.sentiment_counts.negative}</p>
          <p>Neutral: {results.sentiment_counts.neutral}</p>
      </div>
  );
}

export default SentimentResults; // ✅ 修正: デフォルトエクスポートに変更