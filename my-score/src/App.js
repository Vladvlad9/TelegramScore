import './App.css';
import * as React from 'react';
const tg = window.Telegram.WebApp;

function App() {

  const onClose = () =>{
    tg.close()
  }  

  return (
    <div className="App">
      <button onClick={onClose} type="button">Click Me</button>
    </div>
  );
}

export default App;
