import { useContext } from "react";
import { signOut } from "firebase/auth";
import { auth } from "../firebaseConfig";
import { AuthContext } from "../App";

import "./Authbuttons.css";

const SignOutButton = () => {
    const [isAuth, setIsAuth] = useContext(AuthContext);

    const handleSignOut = async () => {
        try {
            await signOut(auth);
            setIsAuth(false);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <button className="signout-button" onClick={handleSignOut}>Sign out</button>
        </div>
    );
}

export default SignOutButton;