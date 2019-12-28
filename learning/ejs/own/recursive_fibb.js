function fibb(n){
    n -= 2;
    let x = 1;
    let seq = [];
    for(let i=0; (i-1) <= n; i+=1){
        if(i<=1){
            seq[i] = x;
        }
        else{
            seq[i] = seq[i-2] + seq[i-1]
        }
    }
    return seq;
}

function fast_fibb(n){
    n -= 2;
    let x = 1;
    let seq = [];
    for(let i=0; (i-1) <= n; i+=1){
        if(i<=1){
            seq[i] = x;
        }
        else{
            seq[i] = seq[i-2] + seq[i-1]
            
        }
    }
    return seq;
}

console.log(fibb(30));
