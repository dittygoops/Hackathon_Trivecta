// src/components/News.jsx
import React from 'react';

// Example data for news headlines and market movers
const newsData = [
    { id: 1, title: "Market reaches all-time highs as tech stocks surge", date: "2024-10-25" },
    { id: 2, title: "Investors eye inflation data as interest rates remain steady", date: "2024-10-24" },
    { id: 3, title: "Oil prices hit $100 a barrel amid global supply concerns", date: "2024-10-23" },
];

const marketMovers = [
    { id: 1, ticker: "AAPL", change: "+3.45%" },
    { id: 2, ticker: "TSLA", change: "-1.23%" },
    { id: 3, ticker: "AMZN", change: "+2.67%" },
];

const News = () => {
    return (
        <div className="news">
            <h2>Recent News Headlines</h2>
            <ul>
                {newsData.map(news => (
                    <li key={news.id}>
                        <span>{news.date} - {news.title}</span>
                    </li>
                ))}
            </ul>
            <h2>Market Movers</h2>
            <ul>
                {marketMovers.map(mover => (
                    <li key={mover.id}>
                        <span>{mover.ticker}: {mover.change}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default News;
