num1=Number(prompt("Enter number 1 "))
num2=Number(prompt("Enter number 2 "))
num3=Number(prompt("Enter number 3 "))

if((num1>num2)&(num1>num3))
{
    if (num2 > num3) {
        alert("number 2 is 2nd largest")
    } else {
        alert("number 3 is second largest")
    }
}
else if((num2>num1)&(num2>num3)) {
    if (num1 > num3) {
        alert("number1 is 2nd largest")
    } else {
        alert("number3 is 2nd largest")
    }
}
else if((num3>num1)&(num3>num2))
{
    if (num1 > num2) {
        alert("number1 is 2nd largest")
    } else {
        alert("number2 is 2nd largest")
    }
}