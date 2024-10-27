import React from 'react';
import './Summary.css';

const Summary = ({ data }) => {
    return (
        <div className={`summary-container ${data.length == 0 ? 'invisible' : ''}`}>
            {data.map((item, index) => (
                <div key={index} className="summary-item">
                    <div>{item.ticker}</div>
                    <div>{Number(item.price).toFixed(2)}</div>
                    <div>{Number(item.quantity).toFixed(2)}</div>
                </div>
            ))}
        </div>
    );
};

export default Summary;