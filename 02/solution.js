const fs = require('fs');

// score for each shape
const scores = {
  X: 1,
  Y: 2,
  Z: 3
};

// // win-loss outcomes for each pair of shapes
// const outcomes = {
//   AX: 0,
//   AY: 6,
//   AZ: 3,
//   BX: 6,
//   BY: 0,
//   BZ: 3,
//   CX: 3,
//   CY: 6,
//   CZ: 0
// };

// FIX: chatgpt can't seem to get these values right so i had to manually write these in
const outcomes = {AX: 0, AY: 6, AZ: 3, BX: 6, BY: 0, BZ: 3, CX: 3, CY: 6, CZ: 0 };

// read the strategy guide from the file
const strategy = fs.readFileSync('strategy_guide.txt', 'utf8').trim();

// split the strategy into rounds
const rounds = strategy.split('\n');

// calculate the total score
let totalScore = 0;
for (let round of rounds) {
  const [opponent, myChoice] = round.split(' ');
  const outcome = outcomes[opponent + myChoice];
  const myScore = scores[myChoice];
  totalScore += myScore + outcome;
}

console.log(totalScore);
