class MathsOp{

    add(){
        console.log("inside no arg")
    }
    add(num){
        console.log("inside one arg method")
    }
    add(num1,num2){
        console.log("inside two arg method")
    }
}
let obj=new  MathsOp()
obj.add()
obj.add(34)
obj.add(20,30)

//only works recently implemented method