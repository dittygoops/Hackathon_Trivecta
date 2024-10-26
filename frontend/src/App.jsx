import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import Home from './pages/Home';
import SignIn from './pages/SignIn';
import IndexBuilder from './pages/IndexBuilder';
import Research from './pages/Research';
import WhaleTracker from './pages/WhaleTracker';
import Keys from './pages/Keys';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/indexbuilder" element={<IndexBuilder />} />
        <Route path="/research" element={<Research />} />
        <Route path="/whaletracker" element={<WhaleTracker />} />
        <Route path="/keys" element={<Keys />} />
      </Routes>
    </Router>
  )
}

export default App;