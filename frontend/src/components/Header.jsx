import React from 'react';
import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';

import { AuthContext } from '../App';
import SignInButton from './SignInButton';
import SignOutButton from './SignOutButton';
import './Header.css';

const Header = () => {
    const [isAuth, setIsAuth] = useContext(AuthContext);
    const navigate = useNavigate();

    function handleHeaderClick(i) {
        switch (i) {
            case 0:
                navigate('/');
                break;
            case 1:
                navigate('/indexbuilder');
                break;
            case 2:
                navigate('/whaletracker');
                break;
            case 3:
                navigate('/research');
                break;
            default:
                break;
        }
    }

    if (isAuth) {
        return (
            <div className='header-container'>
                <div className='site-name' onClick={() => handleHeaderClick(0)}>Trivecta</div>
                <div className='header-tags'>
                    <div className='tag-name' onClick={() => handleHeaderClick(1)}>IndexBuilder</div>
                    <div className='tag-name' onClick={() => handleHeaderClick(2)}>WhaleTracker</div>
                    <div className='tag-name' onClick={() => handleHeaderClick(3)}>Research</div>
                </div>
                <SignOutButton />
            </div>
        );
    }

    return (
        <div className='header-container'>
            <div className='site-name'>Trivecta</div>
            <SignInButton />
        </div>
    );
};

export default Header;
