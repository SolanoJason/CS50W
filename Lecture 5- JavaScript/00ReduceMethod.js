const numbers = [1, 2, 3, 4, 9, 5];

function sump(a, b) {
  return a - b;
}

const sum = numbers.reduce(
  (accumulator, currentValue) => accumulator - currentValue,
  0
);

const sum1 = numbers.reduce(sump, 1);

// console.log(sum1);

// console.log(sum);
var numbers2 = numbers.map(function (s) {
  return s * s;
});

//console.log(numbers2);

const numbers3 = numbers.filter((a) => {
    a > 3;
    return a*a;
});
const numbers4 = numbers.map(a => {
    if(a > 3)
    return a*a;
}); 

console.log(numbers3);
console.log(numbers4);
