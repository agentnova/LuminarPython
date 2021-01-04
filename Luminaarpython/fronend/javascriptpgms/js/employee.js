let employee=[{eid:100,name:"ajay",desig:"devop",join:1981,resign:2003},
		{eid:101,name:"vijay",desig:"devop",join:1992,resign:2008},
		{eid:102,name:"bijoy",desig:"ba",join:1999,resign:2007},
		{eid:103,name:"jhon",desig:"ba",join:1989,resign:2010},
		{eid:104,name:"danie",desig:"qa",join:2009,resign:2014},
		{eid:105,name:"lari",desig:"qa",join:1987,resign:2010}]

console.log("All employees with designation")
var res1=employee.map(ob1=>"Name : "+ob1.name+" , Designation : "+ ob1.desig)
for (item of res1) {
    console.log(item)
}


var res2=employee.filter(ob=>ob.desig=="devop")
console.log("Employees with designation devop")
for (item of res2){
    console.log("Name : "+item["name"])
}

var res3=employee.filter(ob=>ob.join>1980&ob.join<2000)
console.log("Employees worked in 80's")
for(item of res3){
    console.log("Name : "+item["name"])
}

var res4=employee.filter(ob=>(ob.resign-ob.join)>9)
console.log("Employees having experience > 9 years")
for(item of res4){
    console.log("Name : "+item["name"])
}

var res5=employee.sort((obj1,obj2)=>obj1.join-obj2.join)
console.log("Employees sorted by their joining year")
for(item of res5){
    console.log("Name : "+item["name"]+" , Year : "+item["join"])
}

