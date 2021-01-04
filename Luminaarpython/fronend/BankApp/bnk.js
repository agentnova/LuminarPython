class Bank {

    static getAccountDetails(){
        var data={
            test1:{username:"testone",password:"testone",accno:1000,balance:5000},
            test2:{username:"testtwo",password:"testtwo",accno:1001,balance:6000},
            test3:{username:"testthree",password:"testthree",accno:1002,balance:8000},
        }
        return data;
    }
    static login(){
        let uname=document.querySelector("#uname").value;
        let pass=document.querySelector("#pass").value;
        let data=Bank.getAccountDetails();
        if(uname in data){
            let passwd=data[uname]["password"]
            if(pass==passwd){

                window.location.href='userHome.html';
            }
            else {
                alert("Password incorrect")
            }
        }
        else{
            alert("no user")
        }

    }

    static deposit(){
        let lbl=document.querySelector("#bal")
        let user=document.querySelector("#d_uname").value;
        let amount=Number(document.querySelector("#d_amt").value);
        let data=Bank.getAccountDetails()
        if(user in data){
            data[user]['balance']+=amount;
            alert("Available balance : "+data[user]['balance']);

            lbl.innerHTML='<h2>Available Balance : '+data[user]['balance']+'</h2>';
        }
    }

    static withdraw(){
        let lbl=document.querySelector("#bal")
        let user=document.querySelector("#w_uname").value;
        let amount=Number(document.querySelector("#w_amt").value);
        let data=Bank.getAccountDetails();
        if(user in data){
            if(data[user]['balance']>amount) {
                data[user]['balance'] -= amount;
                alert("Available balance : " + data[user]['balance']);
                lbl.innerHTML = '<h2>Available Balance : ' + data[user]['balance'] + '</h2>';
            }
            else {
                alert("Not enough balance")
            }
        }
    }
}
