function checkEmpty(id){
 var val=document.getElementsByName(id)[0];
 if (val==null||val=="")
     alert("please fill value");
}

function validations() {
    checkEmpty('level1');
    checkEmpty('level2');
}

/*
function validations(){
 var name=document.form1.level1.value;
 if (name==null||name=="")
 alert("please fill value")
 return false;
 if(number<2)
 alert("please enter above 2 numbers")
 return false;
 if(number=97 && number=122  || number=46 &&  number=57)
 alert("enter only numbers")
 return false;
}
*/