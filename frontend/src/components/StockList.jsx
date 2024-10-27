import React from 'react';

import Stock from './Stock';

const StockList = ({ stocks }) => (
    <div className="stock-list">
        {stocks.map((stock, index) => (
            <Stock
                key={index}
                name={stock.name}
                description={stock.description}
                risk_score={stock.risk_score}
                growth_potential={stock.growth_potential}
            />
        ))}
    </div>
);

export default StockList;