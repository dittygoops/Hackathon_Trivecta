import React from 'react';
import { useContext } from 'react';

import { AuthContext } from '../App';
import SignInButton from './SignInButton';
import SignOutButton from './SignOutButton';
import './Header.css';

const Header = () => {
    const [isAuth, setIsAuth] = useContext(AuthContext);

    return (
        <div className='header-container'>
            <div className='site-name'>WebTest</div>
            {isAuth ? <SignOutButton /> : <SignInButton />}
        </div>
    );
};

export default Header;