function isEven(x){
    if(x == 0){
        //console.log("ret");
        return true;
    }
    if(x == 1){
        //console.log("ret");
        return false;
    }
    else{
        //console.log("rec");
        if(x > 0){
            return isEven(x-2);
        }
        else{
            return isEven(x+2);
        }
    }
}

console.log(isEven(-68));
