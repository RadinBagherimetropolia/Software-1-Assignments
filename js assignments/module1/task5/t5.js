let year = prompt("Enter the year")
let y = parseInt(year)
if ((y % 4 === 0 && y % 100 !==0) || (y % 400 ===0 )){
    document.write("this is a leap year")
}
else{
    document.write("this is not a leap year")
}