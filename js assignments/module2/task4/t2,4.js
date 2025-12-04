let number = [];
while (true){
    let x = parseInt(prompt("Enter your number or exit with zero"))
    if (x === 0){
        break;
    }
number.push(x)
}
number.sort(function (a, b){
    return b - a;
})
console.log("Numbers from largest to smallest:");
for (let num of number) {
    console.log(num);
}

