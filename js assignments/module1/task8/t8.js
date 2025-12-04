let s = parseInt(prompt("Enter the start year"));
let e = parseInt(prompt("Enter the end year"));
document.write("<ul>");
for ( let year = s ; year <= e ; year++){
    if ((year % 4 === 0 && year % 100 !==0) || (year % 400 ===0 )){
    document.write("<li>"+ year + " is a leap year" + "</li>")
}
}
document.write("</ul>");