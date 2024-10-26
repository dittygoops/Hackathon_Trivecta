import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { createContext, useState, useEffect } from 'react';
import { auth } from './firebaseConfig'; // Import your Firebase auth instance
import { onAuthStateChanged } from 'firebase/auth'; // Firebase auth listener

import Home from './pages/Home';
import SignIn from './pages/SignIn';
import IndexBuilder from './pages/IndexBuilder';
import Research from './pages/Research';
import WhaleTracker from './pages/WhaleTracker';
import Keys from './pages/Keys';

export const AuthContext = createContext(null);

const App = () => {
  const [isAuth, setIsAuth] = useState(null); // Initially null (no auth status known)
  const [loading, setLoading] = useState(true); // Loading state for initial auth check

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setIsAuth(user); // Update the auth state based on the user's authentication status
      setLoading(false); // Stop loading once auth status is set
    });

    // Cleanup the listener when the component unmounts
    return () => unsubscribe();
  }, []);

  if (loading) return <div>Loading...</div>; // Render loading while checking auth status

  return (
    <AuthContext.Provider value={[isAuth, setIsAuth]}>
      <Router>
        <Routes>
          <Route 
            path="/"
            element={isAuth ? <Home /> : <Navigate to="/signin" replace />}
            exact
          />
          <Route
            path="/signin"
            element={isAuth ? <Navigate to="/" replace /> : <SignIn />}
          />
          <Route
            path="/indexbuilder"
            element={isAuth ? <IndexBuilder /> : <Navigate to="/signin" replace />} 
          />
          <Route
            path="/research"
            element={isAuth ? <Research /> : <Navigate to="/signin" replace />} 
          />
          <Route
            path="/whaletracker"
            element={isAuth ? <WhaleTracker /> : <Navigate to="/signin" replace />} 
          />
          <Route
            path="/keys"
            element={isAuth ? <Keys /> : <Navigate to="/signin" replace />} 
          />
        </Routes>
      </Router>
    </AuthContext.Provider>
  );
};

export default App;
