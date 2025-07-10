/*
Notes!!!
1- All columns are equaled in value.
2- x = total_height
3- y = column_height
---------
x = y * column_count
y = x / column_count

*/

//<div> elements number & height & width & section
let section = document.getElementById("columns_section");
let column_count = parseInt(
  window.getComputedStyle(section).getPropertyValue("column-count")
);
let first_div = document.getElementById("first_div");
let second_div = document.getElementById("second_div");
let first_div_height = parseInt(window.getComputedStyle(first_div).height);
let second_div_height = parseInt(window.getComputedStyle(second_div).height);
let first_div_width = parseInt(window.getComputedStyle(first_div).width);
let second_div_width = parseInt(window.getComputedStyle(second_div).width);
//Total height and width
let total_height = first_div_height + second_div_height;
let total_width = parseInt(window.getComputedStyle(section).width);

//Column width & height
let column_height = total_height / column_count;
total_height = column_count * column_height;
let column_width = parseInt(total_width / column_count);

//Print the values to the console
console.log(`Columns = ${column_count}`);
console.log(`First <div> height = ${first_div_height}`);
console.log(`Second <div> height = ${second_div_height}`);
console.log(`First <div> width = ${first_div_width}`);
console.log(`second <div> width = ${second_div_width}`);
console.log(`Total height = ${total_height} px`);
console.log(`Total width = ${total_width}`);
console.log(`Column height = ${column_height} px`);
console.log(`Column width = ${column_width}`);

//Print the values into the spans inside <div> elements
document.getElementById(
  "first_div_span"
).innerHTML = `${first_div_width} * ${first_div_height}`;
document.getElementById(
  "second_div_span"
).innerHTML = `${second_div_width} * ${second_div_height}`;
