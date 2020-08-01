var a = 5;
var b = 10;

function foo(strings, ...values) {
    let y = ("asd","asdasd");
    return y;
}

const x = foo`Sum ${a + b} Product ${a * b} Division ${b / a}`;
console.log(x);