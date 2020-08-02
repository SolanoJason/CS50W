var buttons = document.getElementsByTagName("button");
var bars = document.getElementsByTagName("progress");
// Funcion donde bar es el elemento progress y val es el atributo value
function next(bar, val) {
  if (bar.value >= 100) bar.value = 0;
  else bar.value += val;
}

function stop(bar) {
    clearInterval(bar.interval);
}

function star(bar, val) {
  bar.interval = setInterval(() => next(bar, val), 250);
}
buttons[0].addEventListener("click", () => next(bars[1], 10));
buttons[1].addEventListener("click", () => stop(bars[2]));
buttons[2].addEventListener("click", () => star(bars[2], 10));
