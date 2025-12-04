const ul = document.querySelector("#target")
const l = ["First","Second","Third"]
for (let i of l ){
    let text = i + " item"
    let li = document.createElement("li")
    li.innerText = text
    ul.appendChild(li)
    if ( i === "Second"){
        li.className = "my-item"
    }

}

