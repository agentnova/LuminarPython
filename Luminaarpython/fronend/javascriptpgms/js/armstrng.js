var num=Number(prompt("Enter the number "))
var temp=num
var sum=0
while(num>0){
    var rem=num%10
    sum+=(rem*rem*rem)
    num=parseInt(num/10)
}

print("sum=",sum)
if(sum===temp){
    alert("Its an armstrong number")
}
else {
    alert("not an armstrong number")
}