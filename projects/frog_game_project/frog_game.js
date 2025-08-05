//Define the variables;
let squares = [];
let container = document.getElementById('squares-container');
let frog_url = "frog.png";
let frog;
let frog_width;
let frog_height;
let square_width;
let square_height;
//Elements width and height;
container_width = parseInt(window.getComputedStyle(container).width);
square_width = `${container_width / 3}px`;
square_height = square_width;
frog_width = square_width;
frog_height = frog_width;
let square;
//Whenever the user change the squares input value, Make his required squares;
function change_squares_num() {
    if (square != undefined) {
        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }
    }
    let squares_num = parseInt(document.getElementById('squares-num').value);
    //Make squares;
    let x = 0;
    while (x < squares_num) {
        square = document.createElement('div');
        square.style.width = square_width;
        square.style.height = square_height;
        square.style.backgroundColor = "#00b7ff";
        square.style.border = "1px solid #fff";
        square.class = "square";
        container.appendChild(square);
        squares.push(square);
        x++;
    }
    
}

//Still in coding;

/* function change_frogs_num(){
    let frogs_num = parseInt(document.getElementById('frogs-num').value);
    if (frog != undefined) {
        let y = 0;
        while (y < squares.length) {
            if (squares[y].frog) {
                squares[y].remove(frog);
            }
            y++;
        }
    }

    let x = 0;
    while (x <= frogs_num) {
        let rand_sqr = Math.floor(Math.random() * squares.length);
        frog = document.createElement('img');
        frog.src = frog_url;
        frog.style.width = frog_width;
        frog.style.height = frog_height;
        squares[rand_sqr].appendChild(frog);
        x++;
    }
} */