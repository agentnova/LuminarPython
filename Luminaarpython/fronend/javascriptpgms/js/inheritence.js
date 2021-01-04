class Parent{
    phone(){
        console.log("Parent have 5310")
    }
}
class childone extends Parent{
    c1(){
        console.log("inside child one")
    }
}
class child extends childone{
    c2(){
        console.log("inside child")
    }
}
obj=new child()
obj.phone()
obj.c1()
obj.c2()