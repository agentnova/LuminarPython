class Person {
    setPerson(id,name){
        this.id=id;
        this.name=name;
    }
    getPerson(){
        console.log("id="+this.id)
        console.log("name="+this.name)
    }

}

let obj=new Person()
obj.setPerson(1001,"Arjun");
obj.getPerson()