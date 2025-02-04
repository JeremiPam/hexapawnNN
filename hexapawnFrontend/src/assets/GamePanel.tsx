import React from 'react'
import { Grid, GridItem } from "@chakra-ui/react"
import { Box } from '@chakra-ui/react'
import { Image } from '@chakra-ui/react'

const boxThemeWhite={
  width: 100,
  height: 100,
  borderRadius: 0,
  bg: 'white',
}

const boxThemeBlack={
  ...boxThemeWhite,
  bg: '#808080',
}

const sourceWhite='src/images/whitepawn.png'
const sourceBlack='src/images/blackpawn.png'


const GamePanel: React.FC<{ colors: number[] }> = ({ colors }) => {
  return (
    <Grid templateColumns="repeat(3, 1fr)" gap="6">
          {colors.map((value,index)=>(
            <GridItem><Box sx={index % 2 === 0 ? boxThemeWhite : boxThemeBlack}><Image src={value === 1 ? sourceWhite : (value === -1 ? sourceBlack : '')}/></Box></GridItem>
          ))}
    </Grid>
  )
}

export default GamePanel