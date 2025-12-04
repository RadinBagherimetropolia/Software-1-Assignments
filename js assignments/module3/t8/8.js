document.getElementById("start").onclick = function () {
  const n1 = Number(document.getElementById("num1").value);
  const n2 = Number(document.getElementById("num2").value);
  const op = document.getElementById("operation").value;

  let answer = "";

  if (op === "add") {
    answer = n1 + n2;
  }
  else if (op === "sub") {
    answer = n1 - n2;
  }
  else if (op === "mul") {
    answer = n1 * n2;
  }
  else if (op === "div") {
    answer = n1 / n2;
  }

  document.getElementById("result").textContent = `Result: ${answer}`;
};
