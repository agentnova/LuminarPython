var txt=document.querySelector("#nums");
function display(num) {
    let data=txt.value+num;
    txt.value=data;
}

function clears() {
    txt.value="";
}

function calculate() {
    let data=txt.value;
    let reslt=eval(data)
    txt.value=reslt;

}