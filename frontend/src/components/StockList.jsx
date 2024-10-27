import React, { useState } from 'react';
import Stock from './Stock';
import './StockList.css';

const StockList = ({ stocks }) => {
    const [selectedStocks, setSelectedStocks] = useState([]); // State to track selected stocks

    const handleStockClick = (index) => {
        if (selectedStocks.includes(index)) {
            // If the stock is already selected, remove it from the selection
            setSelectedStocks(selectedStocks.filter(i => i !== index));
        } else {
            // Otherwise, add it to the selection
            setSelectedStocks([...selectedStocks, index]);
        }
    };

    return (
        <div className="stock-list">
            {stocks.map((stock, index) => (
                <Stock
                    key={index}
                    ticker={stock.ticker}
                    description={stock.description}
                    risk_score={stock.risk_score}
                    growth_potential={stock.growth_potential}
                    isSelected={selectedStocks.includes(index)} // Check if stock is selected
                    onClick={() => handleStockClick(index)} // Handle click
                />
            ))}
        </div>
    );
}

export default StockList;
