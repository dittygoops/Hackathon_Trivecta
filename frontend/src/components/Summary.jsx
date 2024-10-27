import React from 'react';
import './Summary.css';

const Summary = ({ data }) => {
    return (
        <div className={`summary-container ${data.length == 0 ? 'invisible' : ''}`}>
            <div className="summary-item">
                <div>Ticker</div>
                <div>Quantity</div>
                <div>Price</div>
            </div>
            {data.map((item, index) => (
                <div key={index} className="summary-item">
                    <div>{item.ticker}</div>
                    <div>{Number(item.quantity).toFixed(2)}</div>
                    <div>{Number(item.price).toFixed(2)}</div>
                </div>
            ))}
        </div>
    );
};

export default Summary;