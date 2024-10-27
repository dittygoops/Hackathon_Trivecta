import { query } from 'firebase/firestore';
import { useState } from 'react';

import './StockQuerySubmission.css';

const StockQuerySubmission = () => {
    const [queryInput, setQueryInput] = useState('');
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("Query submitted:", queryInput);
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
                    <button type="submit" disabled={queryInput.length == 0}>Submit</button>
                </form>
             </div>
        </div> 
    );
};

export default StockQuerySubmission ;