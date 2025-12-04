let num = parseInt(prompt("Enter the number of the participants"));
let participants = [];
for ( let i = 0; i < num ; i++){
    let name = prompt(`Enter name for participants ${i + 1}:`);
    participants.push(name)
}
participants.sort()
document.write("<ol>")
for (let name of participants){
    document.write("<li>" + name + "</li>");
}
document.write("</ol>");
