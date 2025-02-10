import { useState,useEffect } from 'react'
import axios from 'axios'
import { Axios, AxiosResponse } from 'axios'
import './App.css'
import GamePanel from './assets/GamePanel'
import { error } from 'console'



function App() {
  
  const [numbers, setNumbers] = useState([1,1,1,0,0,0,-1,-1,-1])
  const [moves,setMoves] =useState([[6,3],[6,4]])
  const [move,setMove]=useState<number[]>()

  useEffect(()=>{axios({
    method:'GET',
    url:'http://127.0.0.1:8000/'
  }).then((response : AxiosResponse)=>{
    console.log(response.data.board)
    console.log(response.data.moves)
    setNumbers(response.data.board),[]
    setMoves(response.data.moves),[]
  }
  ).catch((error)=>{console.log(error.message)}
);},[])
  
const handleMove = (move:number[])=>{
  setMove(move)
  console.log(move)
}
  return (
    <>
      <GamePanel colors={numbers} moves={moves} onMove={handleMove}/>
    </>
  )
}

export default App
