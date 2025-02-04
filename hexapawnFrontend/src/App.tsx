import { useState } from 'react'
import { Axios } from 'axios'
import './App.css'
import GamePanel from './assets/GamePanel'



function App() {
  const [count, setCount] = useState(0)
  const numbers=[-1,-1,-1,0,0,0,1,1,1]
  return (
    <>
      <GamePanel colors={numbers}/>
    </>
  )
}

export default App
