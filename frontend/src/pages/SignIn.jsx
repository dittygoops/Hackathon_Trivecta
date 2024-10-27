import Header from "../components/Header";

import './Page.css';
import './SignIn.css';

const SignIn = () => {
    return (
      <div className="page">
        <Header />
        <div className="page-content">
          <div className="intro-container">
            <div className="description-container">
              <h1>
                Our Mission:
              </h1>
              <h1>
              Increasing access to financial education and literacy through interactive learning pathways with a focus on experiential learning
              </h1>
            </div>
            <div className="video-container">
              <iframe width="560" height="315" src="https://www.youtube.com/embed/apmfqhyRHDw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
          </div>
        </div>
      </div>
    );
  }
  
  export default SignIn;