import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function SignUp() {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const navigate = useNavigate()

    const handleSignUp = async () => {
        try {
            const response = await axios.post('http://localhost:5000/signup', { username, password })
            console.log(response.data);
            navigate('/signin')
        }
        catch (err) {
            console.error(err)
        }
    }

    return (
        <div className='text-center '>

            <h1 className='font-semibold py-2'>Create your Account</h1>

            <div className='py-2'>
                <label className='mr-2' htmlFor='email'>Email: </label>
                <input className='border-2 p-1 rounded-md' id='email' type='text' placeholder='enter your username' value={username} onChange={e => setUsername(e.target.value)} />
            </div>

            <div className='py-2'>
                <label className='mr-2' htmlFor='password'>Password: </label>
                <input className='border-2 p-1 rounded-md' id='password' type='password' placeholder='enter your password' value={password} onChange={e => setPassword(e.target.value)} />
            </div>

            <div className='pt-3'>
            <button className='rounded-lg p-2 bg-gray-200 hover:bg-black hover:text-white transition-all'  onClick={handleSignUp}>Sign Up</button>
            </div>

        </div>
    )
}

export default SignUp