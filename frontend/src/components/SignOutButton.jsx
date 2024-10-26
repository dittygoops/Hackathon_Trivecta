import { useContext } from "react";
import { signOut } from "firebase/auth";
import { auth } from "../firebaseConfig";
import { AuthContext } from "../App";

import "./Authbuttons.css";

const SignOutButton = () => {
    const [user, setUser] = useContext(AuthContext);

    const handleSignOut = async () => {
        try {
            await signOut(auth);
            setUser(false)
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <button className="signout-button" onClick={handleSignOut}>Sign out</button>
    );
}

export default SignOutButton;