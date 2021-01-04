class Student{
    setStudent(roll,name){
        this.roll=roll;
        this.name=name;
    }
    getStudent(){
        console.log("Roll no="+this.roll)
        console.log("Name="+this.name)
    }

}

let obj=new Student()
obj.setStudent(1001,"Arjun");
obj.getStudent()