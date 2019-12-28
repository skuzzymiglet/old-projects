let coins = [1,10,100,1000];

function coinsFor(x, history=[]){
    let total = 0
    if(history.length < 0){
        total = history.reduce((a,b) => a+b);
    }
    console.log("t", total);
    if(total < x){
        console.log(history);
        for(coin of coins){
            let n = coinsFor(x, history=[...history, coin]) !== null;
            console.log("n", typeof n);
            if(n !== 1){
                return n;
            }
            else{
                console.log("hwde");
            }
        }      
    }
    else if(total >  x){
        return null;
    }
    else{
        return history;
    }
}

console.log([1,3,45].reduce((a,b) => a+b));

console.log(coinsFor(670));
