function coinsFor(x){
    function find(current, history){
        if(current == x){
            return history;
        }
        else if (current > x){
            return null;
        }
        else{
            return find(current + 1, `(${history} + 1`) || find(current * 2, `(${history} * 2`) 
        }
    }
    return find(1, "1")
}

console.log(coinsFor(56))
