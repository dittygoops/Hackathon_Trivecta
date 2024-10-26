import { useContext } from "react";
import { signInWithPopup } from "firebase/auth";
import { auth, googleProvider } from "../firebaseConfig";
import { AuthContext } from "../App";

import "./Authbuttons.css";

const SignInButton = () => {
    const [user, setUser] = useContext(AuthContext);

    const signInWithGoogle = async () => {
        try {
            const result = await signInWithPopup(auth, googleProvider);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <button className="signin-button" onClick={signInWithGoogle}>Continue with Google</button>
    );
}

export default SignInButton;
