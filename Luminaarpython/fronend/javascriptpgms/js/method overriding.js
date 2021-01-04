class parent{
    phone(){
        console.log("parent have nokia phone")
    }

}
class child extends parent{
    phone() {
        console.log("child have mi phone")
    }
}
let obj=new child()
obj.phone()