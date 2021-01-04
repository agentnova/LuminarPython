var hone=document.querySelector("#one");
hone.addEventListener("click",()=>{
    hone.style.color="red";
    hone.textContent="clicked";

})

var htwo=document.querySelector("#two");
htwo.addEventListener("mouseover",()=>{
    htwo.style.color="green";
    htwo.textContent="Mouse is currently over it"
})

var hthree=document.querySelector("#three");
hthree.addEventListener("dblclick",()=>{

    hthree.style.color="blue";
    hthree.textContent="double clicked";
})

var num=document.querySelector("#num").value();
myfun=()=>{
    alert(num);
}