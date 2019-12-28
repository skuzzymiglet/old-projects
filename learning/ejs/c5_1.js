let myArray = [[1,2, 5], [5, 6, 7], 3, 2]

let newArray = myArray.reduce((a, b) => a.concat(b));

console.log(newArray);
