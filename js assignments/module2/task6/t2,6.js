function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}
document.write("<ul>");
let result = 0;
while (result !== 6) {
    result = rollDice();
    document.write("<li>" + result + "</li>");
}
document.write("</ul>");