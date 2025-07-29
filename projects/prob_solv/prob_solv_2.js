/* Dev / MORO
2nd problem solving is solved By JS
Find the possible numbers that can be divided by 3 or 5 for specified number */

let number = 0;
let poss_numbers = []
for (let x = 0; number > x; x++) {
    if (x % 3 == 0 || x % 5 == 0) {
        poss_numbers.push(x);
    }
}
console.log(`The possible numbers are [${poss_numbers}]`);