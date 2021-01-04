let cube=num1=>num1**3;
console.log(cube(3))

var arr=[7,9,5,4,67,9,8,3]
var sq=arr.map(num=>num**2)
console.log(sq)

var evens=arr.filter(num=>num%2==0)
console.log(evens)

var max=arr.reduce((num1,num2)=>num1>num2?num1:num2)
console.log(max)

var sort=arr.sort((num1,num2)=>num2-num1)
console.log(sort)