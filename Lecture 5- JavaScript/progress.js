function Fruit(type){
    this.type = type;
    this.color = "unknown";
}
Fruit.prototype.getInformation = function(){
    return "Type: "+this.type+" and Color: "+this.color;
}
var apple = new Fruit("Apple");
console.log(apple.getInformation(1));