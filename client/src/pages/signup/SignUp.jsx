import React, { useState } from 'react'
import axios from 'axios';

function SignUp() {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')

    const handleSignUp = async () => {
        try {
            const response = await axios.post('http://localhost:5000/signup', { username, password })
            console.log(response);
            console.log(response.data);
        }
        catch (err) {
            setError('invaild data or already signuped user')
        }
    }

    return (
        <div>
            <h1 className='text-3xl'>Sign Up</h1>
            <div>
                <input type='text' placeholder='enter your username' value={username} onChange={e => setUsername(e.target.value)} />
            </div>

            <div>
                <input type='password' placeholder='enter your password' value={password} onChange={e => setPassword(e.target.value)} />
            </div>

            <button onClick={handleSignUp}>Sign Up</button>
            {error && <div>{error}</div>}
        </div>
    )
}

export default SignUp