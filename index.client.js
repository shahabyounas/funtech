requestIdleCallback(start);

function start() {
  incrementBtn.addEventListener("click", incrementNumber);
  decrementBtn.addEventListener("click", decrementNumber);
}

var decrementBtn = document.getElementById("decrementBtn");
var incrementBtn = document.getElementById("incrementBtn");
var number = document.getElementById("number");

function incrementNumber() {
  let num = number.textContent;
  let parseNum = Number(num) + 1;

  number.textContent = parseNum;
}

function decrementNumber() {
  let num = number.textContent;
  let parseNum = Number(num) - 1;

  number.textContent = parseNum;
}
