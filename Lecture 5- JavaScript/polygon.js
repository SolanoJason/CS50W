// function Polygon(arr){
//     this.arr = arr;
//     function perimeter(){
//         let sum = 0;
//         this.arr.forEach((value) => {
//             sum += value;
//         });
//         return sum;
//     }
//     grow() {
//         this.height += 2;
//       }
// }

// var arr = [2,3,2];
// var pol = new Polygon(arr);
// console.log(pol.perimeter);
function Tree(){
    height: 10;
    color: 'green';
    grow() {
      this.height += 2;
    };
  };
  tree.grow();