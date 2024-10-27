import Header from "../components/Header";

import StockQuerySubmission from "../components/StockQuerySubmission";
import StockList from "../components/StockList";

import './IndexBuilder.css';

const IndexBuilder = () => {
    return (
      <div className="page">
        <Header />
        <div className="page-content">
          <div className="left-side">
            <StockQuerySubmission />
            <StockList stocks={[]} />
          </div>
          
          <div className="right-side">
            selected stocks
          </div>
        </div>
      </div>
    );
  }
  
  export default IndexBuilder;