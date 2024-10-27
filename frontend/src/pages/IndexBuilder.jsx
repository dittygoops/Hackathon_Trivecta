import { useState, createContext } from "react";

import Header from "../components/Header";
import StockQuerySubmission from "../components/StockQuerySubmission";
import StockList from "../components/StockList";

import './IndexBuilder.css';

export const StockContext = createContext(null);

const IndexBuilder = () => {
  const [stocks, setStocks] = useState([]);
  const [selectedStocks, setSelectedStocks] = useState([]);

  function reset() {
    setStocks([]);
    setSelectedStocks([]);
  }

  function handleStocksUpdate(stocks) {
    setStocks(stocks);
  }

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
          </div>
        </div>
      </StockContext.Provider>
    </div>
  );
}
  
  export default IndexBuilder;