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
              <p>
                Lorem ipsum odor amet, consectetuer adipiscing elit. Nec fringilla arcu potenti enim fermentum habitasse adipiscing senectus. Torquent porta dictum ligula mollis, fames vestibulum sodales convallis. Dictumst id auctor integer metus dis. Scelerisque ornare viverra ornare dis, fusce curae consectetur. Bibendum commodo aliquet felis congue felis.
                <br/>Pellentesque nam sodales penatibus aenean diam fermentum. Justo lacus placerat semper torquent est venenatis at orci. Fermentum aptent donec senectus dui aliquam rutrum. Ex fames nostra ex tristique ridiculus torquent inceptos arcu euismod. Gravida feugiat felis imperdiet purus vivamus habitant laoreet quam cras. Montes nullam cursus, sollicitudin ornare iaculis platea gravida. Sed torquent bibendum pellentesque nisi suspendisse feugiat faucibus gravida integer. Fames aliquet elementum integer ante torquent ad sociosqu pellentesque tellus.
              </p>
            </div>
            <div className="video-container">
              <iframe width="560" height="315" src="https://www.youtube.com/embed/p7HKvqRI_Bo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
          </div>
        </div>
      </div>
    );
  }
  
  export default SignIn;