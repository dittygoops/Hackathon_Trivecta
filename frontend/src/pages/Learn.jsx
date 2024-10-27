import React, { useState, useEffect, useRef } from 'react';

import Message from '../components/Message';
import Header from '../components/Header';
import sendIcon from '../assets/send-icon.svg';
import sendIconDisabled from '../assets/send-icon-disabled.svg';

import './Page.css';
import './Learn.css';

const Learn = () => {
  const [waitingForResponse, setWaitingForResponse] = useState(false);
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([]);
  const messagesEndRef = useRef(null);
  const messagesContainerRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async (text) => {
    if (text.length === 0) return;

    setWaitingForResponse(true);
    setMessages((prevMessages) => [...prevMessages, <Message text={text} role="user" />]);
    setInputValue('');

    await new Promise(r => setTimeout(r, 2000));

    const newMessage = <Message text={text} role="bot" />;
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setWaitingForResponse(false);
  };

  useEffect(() => {
    const messagesContainer = messagesContainerRef.current;
    const handleScroll = () => {
      if (messagesContainer.scrollTop + messagesContainer.clientHeight >= messagesContainer.scrollHeight) {
        scrollToBottom();
      }
    };

    messagesContainer.addEventListener('scroll', handleScroll);
    return () => {
      messagesContainer.removeEventListener('scroll', handleScroll);
    };
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      sendMessage(inputValue);
    }
  };

  return (
    <div className='page'>
      <Header />
      <div className='page-content'>
        <div className='chat-interface'>
          <div className='messages' ref={messagesContainerRef}>
            {messages}
            <div ref={messagesEndRef} />
          </div>
          <div className={`input-container ${waitingForResponse ? 'disabled' : ''}`}>
            <input
              type="text"
              className="prompt-input"
              value={inputValue}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              placeholder="Type your message and press Enter"
              disabled={waitingForResponse}
            />
            <img
              src={waitingForResponse ? sendIconDisabled : sendIcon}
              alt="Send"
              className="send-icon"
              onClick={() => sendMessage(inputValue)}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Learn;