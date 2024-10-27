import { useState } from 'react';

import './StockQuerySubmission.css';

const StockQuerySubmission = ({reset, handleStocksUpdate}) => {
    const [queryInput, setQueryInput] = useState('');
    const [waitingForResponse, setWaitingForResponse] = useState(false);
    
    const handleSubmit = async (e) => {
        setWaitingForResponse(true);
        reset();
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:5000/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: queryInput }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            console.log(data)
            handleStocksUpdate(data);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
        setWaitingForResponse(false);
    };
    
    return (
        <div className="stock-search-container">
            <div className="stock-search-form">
                <form onSubmit={handleSubmit}>  
                    <input
                        type="text"
                        placeholder="Search the Markets for any Industry, Trend, or Group"
                        value={queryInput}
                        onChange={(e) => setQueryInput(e.target.value)}
                    />
                    <button type="submit" disabled={queryInput.length == 0 || waitingForResponse}>{waitingForResponse ? "Loading" : "Submit"}</button>
                </form>
             </div>
        </div> 
    );
};

export default StockQuerySubmission ;