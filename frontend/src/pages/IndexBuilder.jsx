import { useState, createContext, useContext } from "react";

import Header from "../components/Header";
import StockQuerySubmission from "../components/StockQuerySubmission";
import StockList from "../components/StockList";
import Summary from "../components/Summary";
import { KeyContext } from "../App";

import './IndexBuilder.css';

export const StockContext = createContext(null);

const IndexBuilder = () => {
  const [stocks, setStocks] = useState([]);
  const [selectedStocks, setSelectedStocks] = useState([]);
  const [moneyInput, setMoneyInput] = useState(0);
  const [key, setKey] = useContext(KeyContext);
  const [tradeResponse, setTradeResponse] = useState([]); 

  function reset() {
    setStocks([]);
    setSelectedStocks([]);
  }

  function handleStocksUpdate(stocks) {
    setStocks(stocks);
  }

  const handleTradeClick = async () => {
    const tickers = selectedStocks.map(stock => stock.ticker);
    const tradeData = {
      tickers,
      API_key: key[0],
      API_secret: key[1],
      money: Number(moneyInput)
    };

    console.log(JSON.stringify(tradeData));

    try {
      const response = await fetch('http://localhost:5000/submit_query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(tradeData),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setTradeResponse(data);
    } catch (error) {
      console.error('Error:', error);
      setTradeResponse('Trade failed');
    }
  };

  return (
    <div className="page">
      <Header />
      <StockContext.Provider value={[selectedStocks, setSelectedStocks]}>
        <div className="page-content">
          <div className="left-side">
            <StockQuerySubmission reset={reset} handleStocksUpdate={handleStocksUpdate}/>
            <StockList stocks={stocks}/>
            <button className={`build-etf-button ${stocks.length == 0 ? 'invisible' : ''}`}>Build Index</button>
          </div>
          
          <div className="right-side">
            <StockList stocks={selectedStocks}/>
            <input
              className={`investment-amount ${selectedStocks.length == 0 ? 'invisible' : ''}`}
              type="number"
              placeholder="Enter investment amount"
              value={moneyInput}
              onChange={(e) => setMoneyInput(e.target.value)}
            /> 
            <button className={`invest-button ${selectedStocks.length == 0 ? 'invisible' : ''}`} onClick={handleTradeClick} disabled={Number(moneyInput) == 0}>Invest</button>
            <Summary data={tradeResponse}/>
          </div>
        </div>
      </StockContext.Provider>
    </div>
  );
}
  
  export default IndexBuilder;