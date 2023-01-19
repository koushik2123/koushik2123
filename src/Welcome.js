
import React from 'react';

const Welcome = ({name}) => {
    let sayHi = `Hey ${name}!`;
    let greetMessage = `Welcome to LPU College.`;
    return (
        <div>
            <h1>{sayHi}</h1>
            <h2>{greetMessage}</h2>
        </div>
    );
};

export default Welcome;
