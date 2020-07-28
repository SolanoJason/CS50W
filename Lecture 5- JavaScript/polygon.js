function Polygon(arr){
    this.arr = arr;
    this.perimeter = function(){
        let sum = 0;
        this.arr.foreach((value) => {
            sum += value;
        })
        return sum;
    }
}
var arr = [12,1,1,0];
arr.forEach
/*var rect = new Polygon([12,32,12,12]);
console.log(rect.perimeter());*/