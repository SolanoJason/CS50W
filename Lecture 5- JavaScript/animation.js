var posx = 0;
var posy = 0;
var p = document.getElementById("test");
function move(){
    var div = document.getElementById("box");
    posx += 4;
    if(posx === 4) {
        posx = 0;
        posy += 1;
    }
    div.style.left = posx+"%";
    div.style.top = posy+"%";
    p.innerHTML = div.style.top;  
}
setInterval(move, 500);