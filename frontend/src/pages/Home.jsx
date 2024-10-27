import Header from "../components/Header"; // Importing Header component
import React, { useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LinearScale, CategoryScale, PointElement, LineElement, Filler, Tooltip, Legend } from 'chart.js';
import './Home.css'; // Import the CSS for styling
import { useNavigate } from 'react-router-dom'

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

    const mockArticles = [
      {
          title: "Stock market today: Wall Street closes mostly lower and ends a 6-week winning streak",
          image: "https://dims.apnews.com/dims4/default/836ab60/2147483647/strip/true/crop/3656x2436+0+0/resize/980x653!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2Fdb%2Fd0%2Fa8e6a788af3d7256dcf7224c32c8%2F2197b6d6cef948ffb0ad0d7c76f6f4af",
          link: "https://apnews.com/article/stocks-markets-rates-japan-a41eeb280a3fa7cc5aaa042023f560ef",
      },
      {
          title: "Union Pacific’s profit grows 9% as the railroad delivers more but results fall short of Wall Street",
          image: "https://dims.apnews.com/dims4/default/284ba4e/2147483647/strip/true/crop/3000x1999+0+1/resize/980x653!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2Fc4%2F9d%2Fcd5739a2e3127a20dd125cd031f5%2F375871f45d0f460ebc93916dd98f94e2",
          link: "https://apnews.com/article/union-pacific-railroad-earnings-profit-third-quarter-cb7694eda8d942ce16556878eedb5ac0",
      },

      {
        title: "Stock market today: Wall Street finishes mixed after Tesla soars and IBM slumps",
        image: "https://dims.apnews.com/dims4/default/8af959c/2147483647/strip/true/crop/3949x2631+0+1/resize/980x653!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2Fea%2F62%2Ffb0d29dc453537f31645e24a62f5%2F558966db2f4247d2a0f1ee5597af484d",
        link: "https://apnews.com/article/stocks-markets-rates-bonds-dollar-81c830cd6d465440f3d8f4bfc12d7487",
      },

      {
        title: "Stock market today: Wall Street slumps to a rare 3-day losing streak",
        image: "https://dims.apnews.com/dims4/default/b2751ac/2147483647/strip/true/crop/3776x2516+0+0/resize/980x653!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F7c%2F06%2F69359a4161c0a95d4c666b52d6b0%2F400def85bb094ebb9e03b4bb7588e6ac",
        link: "https://apnews.com/article/stock-markets-rates-tokyo-yen-acd1c0b379dbe53978f2e3e6d05e588e",
      },

      {
        title: "Coke’s quarterly revenue and volumes fall but still beat expectations",
        image: "https://dims.apnews.com/dims4/default/0729cc7/2147483647/strip/true/crop/8640x5757+0+1/resize/980x653!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F8f%2Fc8%2F4698bc32259fdff87874010dddea%2F049db1ea91c74e848df856ef18d96a69",
        link: "https://apnews.com/article/cocacola-earnings-coke-c385344f78ef213a391d3280c40ec4d7",
      },


  ];

  const navigate = useNavigate(); // Initialize the hook

    // Define handleLearnMoreClick inside the component
    const handleLearnMoreClick = () => {
        navigate('/learn'); // Navigate to the Learn More page
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

        <div className="edu">
            <h3>Educational Resources</h3>
            <h2>Finance Word of the Day: Volatility</h2>
            <h4>
                Volatility often refers to the amount of uncertainty or risk related to the size of changes in a security’s value.
                A higher volatility means that a security’s value can potentially be spread out over a larger range of values. 
                This means that the price of the security can move dramatically over a short time period in either direction. 
                A lower volatility means that a security’s value does not fluctuate dramatically, and tends to be steadier.
            </h4>

            <div className="videoContainer">
                <iframe src="https://www.youtube.com/embed/p7HKvqRI_Bo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
                <h5> "Never invest in a business you can't understand" - Warren Buffet </h5>
            </div>

            <div className="videoContainer1">
                <iframe src="https://www.youtube.com/embed/Tv4pkivGvdU" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
                <h5>“ETFs are a ground-breaking, innovative way to invest” – Matt Hougan</h5>
            </div>
        </div>

        <div className="market">
            <h3>Market Overview</h3>
            <div className="articles-container">
                {mockArticles.map((article, index) => (
                    <div className="article-box" key={index}>
                        <img src={article.image} alt={article.title} className="article-image" />
                        <h4 className="article-title">{article.title}</h4>
                        <a href={article.link} target="_blank" rel="noopener noreferrer" className="article-link">
                            Read more
                        </a>
                    </div>
                ))}
            </div>

            {/* Learn More Button */}
            <div className="button-container">
            <button className="learn-more-button" onClick={handleLearnMoreClick}>
                Questions? Ask our Trivecta AI
            </button>
            </div>
        </div>
    </div>
);
};

export default Home;