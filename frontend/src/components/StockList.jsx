import React, { useState, useContext } from 'react';

import { StockContext } from '../pages/IndexBuilder';
import Stock from './Stock';

import './StockList.css';

const StockList = ({ stocks }) => {
    const [selectedStocks, setSelectedStocks] = useContext(StockContext);

    const handleStockClick = (index) => {
        const selectedStock = stocks[index];
        if (selectedStocks.some(stock => stock.ticker === selectedStock.ticker)) {
            // If the stock is already selected, remove it from the selection
            setSelectedStocks(selectedStocks.filter(stock => stock.ticker !== selectedStock.ticker));
        } else {
            // Otherwise, add it to the selection
            setSelectedStocks([...selectedStocks, selectedStock]);
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
                    isSelected={selectedStocks.includes(stocks[index])} // Check if stock is selected
                    onClick={() => handleStockClick(index)} // Handle click
                />
            ))}
        </div>
    );
}

export default StockList;
