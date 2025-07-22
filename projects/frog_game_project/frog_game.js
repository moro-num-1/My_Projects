//Define the variables;
let container = document.getElementById('squares_container');
let squares_num;
let square_width;
let square_height;

//Elements width and height;
container_width = parseInt(window.getComputedStyle(container).width);
square_width = container_width / 3;
square_height = square_width;

//When the user change the input value;
function change_squares_num() {
    squares_num = document.getElementById('squares_num').value;
    console.log(`squares = ${squares_num}`);
    //Make squares;
    let x;
    while (x < squares_num) {
        let square = document.createElement('div');
        square.style.width = square_width;
        square.style.height = square_height;
        container.appendChile(square);
        x++;
    }
}