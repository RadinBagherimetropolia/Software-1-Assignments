let one = prompt("Enter the first number");
let two = prompt("Enter the second number");
let three = prompt("Enter the third number");
let one_int = parseInt(one);
let two_int = parseInt(two);
let three_int = parseInt(three);

const sum = one_int + two_int + three_int;
const product = one_int * two_int * three_int;
const ave = sum/3;
document.write("sum is: " + sum + "<br>");
document.write("product is: " + product + "<br>");
document.write("average is:" + ave + "<br>");