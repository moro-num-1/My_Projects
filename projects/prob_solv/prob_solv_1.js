//Dev / MORO;
//First problem solving is solved by JS;
//Print the heist number in an array;

let numbers = [3, 7, 5, 1];
let heist_number = numbers[1]
for (let x = 0; x < numbers.length; x++) {
    if (heist_number < numbers[x]) {
        heist_number = numbers[x];
    }
}
console.log(`The heist number in the array is ${heist_number}`);