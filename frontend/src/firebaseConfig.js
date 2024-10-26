// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth"; // Import Firebase Auth service

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCx3_LZeZ1jHXwpvW8I4L4XUNf4Mnr7DYo",
    authDomain: "hackathon-trivecta.firebaseapp.com",
    projectId: "hackathon-trivecta",
    storageBucket: "hackathon-trivecta.appspot.com",
    messagingSenderId: "625428634867",
    appId: "1:625428634867:web:a3cd7cd6037860e88b6b86"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();

export { auth, googleProvider};