import { useState, createContext, useContext } from "react";

import Header from "../components/Header";
import StockQuerySubmission from "../components/StockQuerySubmission";
import StockList from "../components/StockList";
import { KeyContext } from "../App";

import './IndexBuilder.css';

export const StockContext = createContext(null);

const IndexBuilder = () => {
  const [stocks, setStocks] = useState([]);
  const [selectedStocks, setSelectedStocks] = useState([]);
  const [moneyInput, setMoneyInput] = useState(0);
  const [key, setKey] = useContext(KeyContext);
  const [tradeResponse, setTradeResponse] = useState(''); 

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
      key: key[0],
      secret: key[1],
      money: moneyInput
    };

    console.log(JSON.stringify(tradeData));

    // try {
    //   const response = await fetch('http://localhost:5000/get-order', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify(tradeData),
    //   });

    //   if (!response.ok) {
    //     throw new Error('Network response was not ok');
    //   }

    //   const data = await response.json();
    //   setTradeResponse(data.message || 'Trade successful');
    // } catch (error) {
    //   console.error('Error:', error);
    //   setTradeResponse('Trade failed');
    // }
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
            <button className={`invest-button ${selectedStocks.length == 0 ? 'invisible' : ''}`} onClick={handleTradeClick} disabled={moneyInput.length == 0 ? 'disabled' : ''}>Invest</button>
            <div className={`trade-response ${selectedStocks.length == 0 ? 'invisible' : ''}`}>{tradeResponse}</div>
          </div>
        </div>
      </StockContext.Provider>
    </div>
  );
}
  
  export default IndexBuilder;