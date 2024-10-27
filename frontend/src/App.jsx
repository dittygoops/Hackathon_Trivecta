import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { createContext, useState, useEffect } from 'react';
import { auth } from './firebaseConfig'; // Import your Firebase auth instance
import { onAuthStateChanged } from 'firebase/auth'; // Firebase auth listener
import { getFirestore, doc, getDoc, setDoc } from "firebase/firestore"; // Firestore imports

import Home from './pages/Home';
import SignIn from './pages/SignIn';
import IndexBuilder from './pages/IndexBuilder';
import Learn from './pages/Learn';
import WhaleTracker from './pages/WhaleTracker';
import Keys from './pages/Keys';

import './App.css';

export const AuthContext = createContext(null);
export const KeyContext = createContext(null);

const App = () => {
  const [user, setUser] = useState(null); // Initially null (no auth status known)
  const [key, setKey] = useState(null);
  const [loading, setLoading] = useState(true); // Loading state for initial auth check

  const db = getFirestore(); // Initialize Firestore

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      setUser(user); // Update the auth state based on the user's authentication status

      if (user) {
        // Fetch the key data for the authenticated user
        const userRef = doc(db, "users", user.uid);
        const userDoc = await getDoc(userRef);
        
        if (userDoc.exists()) {
          setKey(userDoc.data().alpacaKey); // Set the key variable if it exists
        } else {
          setKey(null); // Set key to null if no entry exists
        }
      } else {
        setKey(null); // Clear the key if no user is authenticated
      }

      setLoading(false); // Stop loading once auth status is set
    });

    // Cleanup the listener when the component unmounts
    return () => unsubscribe();
  }, []);

  if (loading) return <div>Loading...</div>; // Render loading while checking auth status

  return (
    <AuthContext.Provider value={[user, setUser]}>
      <KeyContext.Provider value={[key, setKey]}>
        <Router>
          <Routes>
            <Route 
              path="/"
              element={user ? (
                key ? <Home /> : <Navigate to="/keys" replace />
              ) : <Navigate to="/signin" replace />}
            />
            <Route
              path="/signin"
              element={user ? <Navigate to="/" replace /> : <SignIn />}
            />
            <Route
              path="/indexbuilder"
              element={user ? (
                key ? <IndexBuilder /> : <Navigate to="/keys" replace />
              ) : <Navigate to="/signin" replace />} 
            />
            <Route
              path="/learn"
              element={user ? (
                key ? <Learn /> : <Navigate to="/keys" replace />
              ) : <Navigate to="/signin" replace />}
            />
            <Route
              path="/whaletracker"
              element={user ? (
                key ? <WhaleTracker /> : <Navigate to="/keys" replace />
              ) : <Navigate to="/signin" replace />}
            />
            <Route
              path="/keys"
              element={user ? (
                key ? <Navigate to="/" replace /> :  <Keys />
              ) : <Navigate to="/signin" replace />}
            />
          </Routes>
        </Router>
      </KeyContext.Provider>
    </AuthContext.Provider>
  );
};

export default App;
