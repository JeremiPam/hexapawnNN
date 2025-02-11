import { useState,useEffect } from 'react'
import axios from 'axios'
import { Axios, AxiosResponse } from 'axios'
import './App.css'
import GamePanel from './assets/GamePanel'
import { error } from 'console'
import { Button } from '@chakra-ui/react'



function App() {
  
  const [numbers, setNumbers] = useState([0,0,0,0,0,0,0,0,0])
  const [moves,setMoves] =useState<number[][]>([[6,4]])
  const [move,setMove]=useState<number[]>()
  const [newGame,setNewgame]=useState<Boolean>()
  useEffect(()=>{
    axios({
    method:'GET',
    url:'http://127.0.0.1:8000/position'
  }).then((response : AxiosResponse)=>{
    console.log(response.data.board)
    console.log(response.data.moves)
    console.log("winner",response.data.winner)
    setNumbers(response.data.board),[]
    setMoves(response.data.moves),[]
  }
  ).catch((error)=>{console.log(error.message)}
);},[move])
  
const handleNewGame = ()=>{
  axios.post('http://127.0.0.1:8000/newGame', {
    setNewGame:true
})
.then(function (response) {
  console.log(response);
  setNewgame(!newGame)
  setMove(undefined)
})
.catch(function (error) {
  console.log(move);
});
}

const handleMove = (move:number[])=>{
  
  console.log(move)
  axios.post('http://127.0.0.1:8000/move', {
    first:move[0],
    target:move[1],
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(move);
  })
  setMove(move)
}
  return (
    <>
      <GamePanel colors={numbers} moves={moves} onMove={handleMove}/>
      <Button onClick={handleNewGame}>New game</Button>
    </>
  )
}

export default App
