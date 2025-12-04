let dog = []
for ( let name = 0 ; name <6 ; name++){
    let i = prompt(`Enter the name ${name + 1}`)
    dog.push(i)
}
let b = dog.sort();
let x = dog.reverse();
document.write("<ul>");
document.write(x);
document.write("</ul>");