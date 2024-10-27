import { useState } from "react";

import Header from "../components/Header";
import StockQuerySubmission from "../components/StockQuerySubmission";
import StockList from "../components/StockList";

import './IndexBuilder.css';

const IndexBuilder = () => {
  const [stocks, setStocks] = useState([]);
  const [selectedStocks, setSelectedStocks] = useState([]);

  function handleStocksUpdate(stocks) {
    setStocks(stocks);
  }

  return (
    <div className="page">
      <Header />
      <div className="page-content">
        <div className="left-side">
          <StockQuerySubmission handleStocksUpdate={handleStocksUpdate}/>
          <StockList stocks={stocks} />
          <button className={`build-etf-button ${stocks.length == 0 ? 'invisible' : ''}`}>Build Index</button>
        </div>
        
        <div className="right-side">
          selected stocks
        </div>
      </div>
    </div>
  );
}
  
  export default IndexBuilder;