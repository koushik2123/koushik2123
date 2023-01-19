import React from "react";
import './App.css';
import { useState } from "react";
import Welcome from './Welcome';
function App() {
  const [name, setName] = useState("")
  const [Login, setLogin] = useState(false)
  return (

  <div>
    <div>
      <label>Name: </label>
      <input type="text" placeholder="Enter Your Name" value={name}
       onChange={(event)=>{setName(event.target.value)}}></input>
          </div>
          <div><button onClick={()=>{setLogin(!Login)}}>Login</button></div>
          {(Login && name) && <Welcome name={name}></Welcome>}
          </div>
  );
}



export default App;
