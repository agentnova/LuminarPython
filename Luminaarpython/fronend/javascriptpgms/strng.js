var txt="HHHPPSDAAA"
var dict={}
var out=""

for(i=0;i<txt.length;i++){
    if(txt[i] in dict){
        dict[txt[i]]+=1;
    }
    else {
        dict[txt[i]]=1;
    }
}
for(item in dict){
    out+=dict[item]+item;
}
console.log(out)

