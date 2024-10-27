import Header from "../components/Header";


const investors = [
  {
      name: "Warren Buffett",
      portfolio: [
          { stock: "Apple Inc.", shares: 100000000, value: "$13.5B" },
          { stock: "Bank of America", shares: 100000000, value: "$28.1B" },
          { stock: "Coca-Cola", shares: 400000000, value: "$23.2B" },
      ],
  },
  {
      name: "Cathie Wood",
      portfolio: [
          { stock: "Tesla Inc.", shares: 5000000, value: "$4.5B" },
          { stock: "Square Inc.", shares: 8000000, value: "$2.3B" },
          { stock: "Zoom Video", shares: 3000000, value: "$1.1B" },
      ],
  },
  {
      name: "Bill Ackman",
      portfolio: [
          { stock: "Restaurant Brands", shares: 4000000, value: "$4.2B" },
          { stock: "Air Products", shares: 5000000, value: "$1.3B" },
          { stock: "Universal Music Group", shares: 7000000, value: "$1.5B" },
      ],
  },
];

// Sample data for recent congressional trades (update with real data as needed)
const congressionalTrades = [
  {
      name: "Senator John Doe",
      stock: "XYZ Corp.",
      date: "2024-10-15",
      value: "$250,000",
  },
  {
      name: "Representative Jane Smith",
      stock: "ABC Ltd.",
      date: "2024-10-16",
      value: "$150,000",
  },
  {
      name: "Senator Mike Johnson",
      stock: "LMN Inc.",
      date: "2024-10-17",
      value: "$300,000",
  },
];

const WhaleTracker = () => {

    return (
      <div>
        <Header />
        <div className="whale-tracker" style={{ backgroundColor: 'black', color: 'white', padding: '20px' }}>
            <h1>Whale Tracker</h1>

            <div className="investors-container">
                {investors.map((investor, index) => (
                    <div className="investor-column" key={index}>
                        <h2>{investor.name}</h2>
                        <ul>
                            {investor.portfolio.map((investment, idx) => (
                                <li key={idx}>
                                    <span>{investment.stock}: </span>
                                    <span>{investment.shares} shares, valued at {investment.value}</span>
                                </li>
                            ))}
                        </ul>
                    </div>
                ))}
            </div>

            <div className="congressional-trades">
                <h2>Recent Congressional Trades</h2>
                <ul>
                    {congressionalTrades.map((trade, index) => (
                        <li key={index}>
                            <span>{trade.name} sold {trade.stock} on {trade.date} for {trade.value}</span>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
      </div>
    );
  }
  
  export default WhaleTracker;
