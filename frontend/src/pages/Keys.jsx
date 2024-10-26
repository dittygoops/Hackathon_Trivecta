import Header from "../components/Header";
import KeySubmission from "../components/KeySubmission";

import './Page.css';

const Keys = () => {
    return (
      <div className="page">
        <Header />
        <div className="page-content">
          <KeySubmission />
        </div>
      </div>
    );
  }
  
  export default Keys;