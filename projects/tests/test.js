/*
Notes:-

1- x = total_height;
2- y = column_height;
3- column_count = any positive whole number;
*/

// let number = (Math.random() * 100);
// number_string = number.toString();
// let dot_index = number_string.indexOf(".");
// let floored_number = number - parseFloat(`0${number_string.slice(dot_index, )}`);
// console.log(floored_number);

let min = 0;
let max = 5;
let column_count = parseInt(Math.random() * max);
let x;
let y;

x = y * column_count;
y = x / column_count;

console.log(y);
