import { getFirestore, doc, setDoc } from "firebase/firestore"; // Import necessary Firestore functions
import { useState, useContext } from "react";
import { AuthContext } from "../App";
import { KeyContext } from "../App";
import { useNavigate } from "react-router-dom";

import './KeySubmission.css';

const KeySubmission = () => {
    const [keyInput, setKeyInput] = useState('');
    const [key, setKey] = useContext(KeyContext);
    const [user, setUser] = useContext(AuthContext);
    const navigate = useNavigate();

    const db = getFirestore(); // Initialize Firestore
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (user) {
            const userRef = doc(db, "users", user.uid);
            try {
              await setDoc(userRef, { alpacaKey: keyInput }, { merge: true }); // Write the alpacaKey to Firestore
              setKey(keyInput); // Update the key state variable
              navigate("/"); // Redirect to the home page
            } catch (error) {
              console.error("Error writing alpacaKey to Firestore:", error);
            }
        } else {
            console.log("No user is authenticated.");
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
                        value={keyInput}
                        onChange={(e) => setKeyInput(e.target.value)}
                    />
                    <button type="submit" disabled={keyInput.length == 0}>Submit</button>
                </form>
             </div>
        </div> 
    );
};

export default KeySubmission;