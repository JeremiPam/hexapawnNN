import React from 'react';
import { Grid, GridItem } from "@chakra-ui/react";
import { Box } from '@chakra-ui/react';
import { Image } from '@chakra-ui/react';
import { useState } from "react";

const boxThemeWhite = {
  width: 100,
  height: 100,
  borderRadius: 0,
  bg: '#f0d9b5',
};

const boxThemeBlack = {
  ...boxThemeWhite,
  bg: '#946f51',
};

const boxThemeYellow = {
  ...boxThemeWhite,
  bg: 'yellow',
};

const sourceWhite = 'src/images/whitepawn.png';
const sourceBlack = 'src/images/blackpawn.png';

interface GamePanelProps {
  colors: number[];
  moves: number[][];
  onMove: (move: number[]) => void;
}

const GamePanel: React.FC<GamePanelProps> = ({ colors, moves, onMove }) => {
  const [board, setBoard] = useState(colors);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);

  const handleClick = (index: number) => {
    if (selectedIndex === null) {
      setSelectedIndex(index);
    } else {
      const isMoveValid = moves.some(move => move[0] === selectedIndex && move[1] === index);

      if (isMoveValid) {
        onMove([selectedIndex, index]);
      }
      setSelectedIndex(null);
    }
  };

  const getPossibleMoves = (index: number) => {
    const possibleMoves = moves.filter(move => move[0] === index).map(move => move[1]);
    return possibleMoves;
  };

  const possibleMoves = selectedIndex !== null ? getPossibleMoves(selectedIndex) : [];

  return (
    <>
      <div>moves: {JSON.stringify(moves)}</div>
      <Grid templateColumns="repeat(3, 1fr)" gap="6">
        {colors.map((value, index) => (
          <GridItem key={index}>
            <Box
              sx={
                possibleMoves.includes(index)
                  ? boxThemeYellow
                  : index % 2 === 0
                  ? boxThemeWhite
                  : boxThemeBlack
              }
              onClick={() => handleClick(index)}
            >
              <Image key={index} src={value === 1 ? sourceWhite : (value === -1 ? sourceBlack : '')} />
            </Box>
          </GridItem>
        ))}
      </Grid>
    </>
  );
};

export default GamePanel;