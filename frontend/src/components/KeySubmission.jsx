import { useState } from "react";

import './KeySubmission.css';

const KeySubmission = () => {
    const [key, setKey] = useState('');
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/keys', { key });
            setMessage(response.data.message);
        } catch (error) {
            setMessage(error.response.data.message);
        }
    };
    
    return (
        <div className="key-form-container">
            <div className="key-form-title">
                Alpaca Key Submission
            </div>
            <div className="key-form-description"> 
                We use Alpaca as a service to complete trades for you. Please enter your Alpaca API key below.
            </div>
            <div className="key-form">
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder="Enter your Alpaca API key"
                        value={key}
                        onChange={(e) => setKey(e.target.value)}
                    />
                    <button type="submit">Submit</button>
                </form>
             </div>
        </div> 
    );
};

export default KeySubmission;