var heads=document.getElementsByTagName("h2");
for(hd of heads){
    hd.style.color="red";
}

var uls=document.getElementsByTagName("ul");
for(ul of uls){
    ul.style.color="blue";
}

var headss=document.querySelectorAll("h1");
for(hs of headss){
    hs.style.color="yellow";
}

var lst=document.querySelectorAll("li")
for(it of lst){
    it.textContent="listem";
}
