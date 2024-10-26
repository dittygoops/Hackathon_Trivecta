import { useContext } from "react";
import { signInWithPopup } from "firebase/auth";
import { auth, googleProvider } from "../firebaseConfig";
import { AuthContext } from "../App";

import "./Authbuttons.css";

const SignInButton = () => {
    const [isAuth, setIsAuth] = useContext(AuthContext);

    const signInWithGoogle = async () => {
        try {
            await signInWithPopup(auth, googleProvider);
            setIsAuth(true);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <button className="signin-button" onClick={signInWithGoogle}>Continue with Google</button>
        </div>
    );
}

export default SignInButton;
