function fact(num){
    var fact=1;
    var i=1;
    while (i<=num){
        fact*=i;
        i++;
    }
    alert("Factorial of "+num+"="+fact)

}

n=Number(prompt("enter number"))
fact(n)