let coins = [1, 2, 5, 10, 20, 50, 100, 500, 10000]

function coinsFor(val, prev=[]){
    if(prev != []){
        let sum = prev.reduce((a, b) => a + b)
    }
    else{
        return coinsFor(val, prev=prev)
    }
    if(sum == val){
        return prev
    }
    else if(sum >= val){
        return false
    }
    else{
        return coinsFor(val, prev=[prev, ])
    }
}

console.log(coinsFor(670))
