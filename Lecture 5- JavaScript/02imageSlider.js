var imgs = [
  "http://www.sololearn.com/uploads/slider/1.jpg",
  "http://www.sololearn.com/uploads/slider/2.jpg",
  "http://www.sololearn.com/uploads/slider/3.jpg",
];
var prev = document.getElementById("prev");
var next = document.getElementById("next");
var img = document.getElementById("img");
var p = document.getElementById("imgsrc");
var pos = 0;
function pre() {
  pos -= 1;
  if (pos == -1) {
    pos = imgs.length-1;
  }
  img.src = imgs[pos];
  p.innerHTML = imgs[pos] + " " + pos;
}
function nex() {
  pos += 1;
  if (pos == imgs.length) {
    pos = 0;
  }
  img.src = imgs[pos];
  p.innerHTML = imgs[pos] + " " + pos;
}
prev.addEventListener("click", pre);
next.addEventListener("click", nex);
