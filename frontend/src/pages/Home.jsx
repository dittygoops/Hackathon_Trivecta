import Header from "../components/Header"; // Importing Header component
import React, { useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LinearScale, CategoryScale, PointElement, LineElement, Filler, Tooltip, Legend } from 'chart.js';
import './Home.css'; // Import the CSS for styling

// Register Chart.js components
ChartJS.register(LinearScale, CategoryScale, PointElement, LineElement, Filler, Tooltip, Legend);

const Home = () => {
    // State for Portfolio Overview
    const [portfolioBalance] = useState(100000.00); // Example balance
    const [portfolioData] = useState({
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], // Category labels
        datasets: [
            {
                label: 'Portfolio Value',
                data: [100000, 100200, 100150, 100350, 100675],
                fill: false,
                backgroundColor: '#FFC107',
                borderColor: '#FFC107',
            },
        ],
    });

    // Calculate Total Profit on the Day
    const initialValue = portfolioData.datasets[0].data[0]; // Initial value of the portfolio
    const currentValue = portfolioData.datasets[0].data[portfolioData.datasets[0].data.length - 1]; // Latest value
    const totalProfit = currentValue - initialValue; // Calculate profit
    const profitColor = totalProfit >= 0 ? 'green' : 'red'; // Determine color based on profit

    // State for Watchlist
    const [stocks] = useState([
        { name: "Apple Inc.", symbol: "AAPL", price: 231.41, change: 0.36 },
        { name: "Microsoft Corp.", symbol: "MSFT", price: 428.15, change: 0.81 },
        { name: "Tesla Inc.", symbol: "TSLA", price: 269.19, change: 3.34 },
        { name: "Amazon.com Inc.", symbol: "AMZN", price: 187.83, change: 0.78 },
        { name: "Meta Platforms, Inc.", symbol: "META", price: 573.25, change: 0.96 },
        { name: "NVIDIA Corporation", symbol: "NVDA", price: 141.54, change: 0.80 },
        { name: "Alphabet Inc.", symbol: "GOOGL", price: 165.27, change: 1.57 },
        { name: "Berkshire Hathaway Inc.", symbol: "BRK.B", price: 454.01, change: -0.81 },
        { name: "Visa Inc.", symbol: "V", price: 281.73, change: -0.54 },
        { name: "JPMorgan Chase & Co.", symbol: "JPM", price: 222.31, change: -1.19 },
        { name: "Walmart Inc.", symbol: "WMT", price: 82.51, change: -0.65 },
        { name: "Johnson & Johnson", symbol: "JNJ", price: 160.88, change: -1.70 },
        { name: "Procter & Gamble Co.", symbol: "PG", price: 168.22, change: -0.83 },
        { name: "Coca-Cola Co.", symbol: "KO", price: 66.92, change: -0.56 },
        { name: "PepsiCo, Inc.", symbol: "PEP", price: 171.79, change: -0.21 },
        { name: "Netflix, Inc.", symbol: "NFLX", price: 754.68, change: 0.017 },
        { name: "Intel Corporation", symbol: "INTC", price: 22.68, change: 1.52 },
        { name: "Adobe Inc.", symbol: "ADBE", price: 483.72, change: 0.18 },
        { name: "Salesforce, Inc.", symbol: "CRM", price: 290.46, change: 1.32 },
        { name: "IBM Corporation", symbol: "IBM", price: 214.67, change: -1.70 },
        { name: "PayPal Holdings, Inc.", symbol: "PYPL", price: 81.70, change: 0.38 },
        { name: "Palantir Technologies Inc", symbol: "PLTR", price: 44.86, change: 2.96 },
        { name: "Carvana Co", symbol: "CVNA", price: 202.53, change: 1.15 },
        { name: "Rivian Automotive Inc.", symbol: "RIVN", price: 10.45, change: 0.19 },
    ]);

    // Chart options
    const options = {
        responsive: true,
        scales: {
            y: {
                beginAtZero: false,
                ticks: {
                    color: '#ffffff', // Set y-axis label color to white
                },
                grid: {
                    color: '#888888', // Set y-axis grid line color to gray
                },
            },
            x: {
                ticks: {
                    color: '#ffffff', // Set x-axis label color to white
                },
                grid: {
                    color: '#888888', // Set x-axis grid line color to gray
                },
            },
        },
        plugins: {
            legend: {
                labels: {
                    color: '#ffffff', // Set legend label color to white
                },
            },
            tooltip: {
                titleColor: '#ffffff', // Set tooltip title color to white
                bodyColor: '#ffffff', // Set tooltip body color to white
                borderColor: '#ffffff', // Set tooltip border color to white
                borderWidth: 1, // Optional: Set tooltip border width
            },
        },
    };

    return (
      <div className="home">
          <Header />
          <h1>Portfolio Dashboard</h1>
          <div className="home-content">
              <div className="portfolio-overview">
                  <h2>Portfolio Overview</h2>
                  <p>Balance: ${portfolioBalance.toFixed(2)}</p>
                  <div className="chart-container">
                      <Line data={portfolioData} options={options} />
                  </div>
                  {/* Total Profit on the Day */}
                  <div className="profit-box">
                      <h2>Total Profit on the Day</h2>
                      <p className="profit-amount">${(portfolioData.datasets[0].data[portfolioData.datasets[0].data.length - 1] - portfolioBalance).toFixed(2)}</p>
                  </div>
              </div>
  
              <div className="watchlist">
                  <h2>Your Watchlist</h2>
                  <div className="watchlist-grid">
                      {stocks.map((stock) => (
                          <div className="watchlist-item" key={stock.symbol}>
                              <div>
                                  <strong>{stock.name}</strong> ({stock.symbol})
                              </div>
                              <div className="stock-price">${stock.price.toFixed(2)}</div>
                              <div className={`stock-change ${stock.change >= 0 ? 'green' : 'red'}`}>
                                  {stock.change >= 0 ? `+${stock.change.toFixed(2)}%` : `${stock.change.toFixed(2)}%`}
                              </div>
                          </div>
                      ))}
                  </div>
              </div>
          </div>
      </div>
  );
};

export default Home;
