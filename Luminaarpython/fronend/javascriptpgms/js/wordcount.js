var line="HELLO HAI HELLO HAI"
var words=line.split(" ")
var dict={}

for(word of words){
    if(word in dict){
        dict[word]+=1;
    }
    else {
        dict[word]=1;
    }
}
for(item in dict){
    console.log(item+" : "+dict[item])
}






// for (i=0;i<words.length;i++){
//     if(words[i] in dict){
//
//         dict[words[i]]+=1;
//     }
//     else{
//         dict[words[i]]=1;
//     }
// }
// for(item in dict){
//     console.log(item+" : "+dict[item])
// }



// for word in words:
//     if(word not in dict):
//         dict[word]=1
//     else:
//         dict[word]+=1
// print(dict)