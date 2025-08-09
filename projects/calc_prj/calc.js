let elements = document.body.children;
for (let element of elements) {
    if (element.className === "opr") {
        console.log("I'm an operation.")
    }
}