class Book {
    constructor(id,name,pageno,price) {
        this.id=id;
        this.name=name;
        this.pageno=pageno;
        this.price=price;
    }
    getBook(){
        console.log(this.name)
        console.log(this.id);
    }

}
let obj=new Book(1,"book1",100,40)
let obj1=new Book(2,"book2",200,800)
let obj2=new Book(3,"book3",300,700)
let obj3=new Book(4,"book4",400,70)

var arr=[]

arr.push(obj)
arr.push(obj1)
arr.push(obj2)
arr.push(obj3)


var bk=arr.filter(ob=>ob.price>250)

for(item of bk){
    console.log("Book with price > 250 : "+item.name)
}

var maxs=arr.map(obj=>obj.price).reduce((p1,p2)=>p1>p2?p1:p2)
console.log("Book with max price : "+maxs)

var upp=arr.map(obj=>obj.name.toUpperCase())
console.log(upp)






// for(item of arr){
//     var upp=item["name"].toUpperCase()
//     console.log(upp)
// }



