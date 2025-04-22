import React from "react";
import { useState } from "react";


export const Login = () => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const getEmail = (e) => {
        e.preventDefault()
        setEmail(e.target.value)
    }
    
    const getPassword = (e) => {
        e.preventDefault()
        setPassword(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        
    }
    return (<div>
        <form>
            <div className="mb-3">
                <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                <input onChange= {getEmail} type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" value={email}/>
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div className="mb-3">
                <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                <input onChange={getPassword} type="password" className="form-control" id="exampleInputPassword1" value={password}/>
            </div>
                <button onClick={handleSubmit} type="submit" className="btn btn-primary">Submit</button>
        </form>        
</div>)
}
