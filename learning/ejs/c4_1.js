function range(start, end, step=1){
    let x = [];
    if(step >= 0){
        for(let i = start; i <= end; i += step){
            x.push(i);
        }
    }
    else{
        for(let i = start; i >= end; i += step){
            x.push(i);
        }
    }
    return x;
}

function reverseArray(x){
    let y = [];
    for(let i of range(x.length-1, 0, step=-1)){
        y.push(x[i]);
    }
    return y;
}

function reverseArrayInPlace(x){
    let full = x
    for(let i of range(0, x.length-1)){
        console.log(full[i], x);
        x[i] = full[x.length-1 - i];
        console.log("too", full[i], x);
    }
}

arr = [1, 2, 3, 4, 5];
reverseArrayInPlace(arr);
console.log(arr);
