function reverseArray(x){
    let res = [];
    for(let i = x.length-1; i >= 0; i--){
        res.push(x[i])
    }
    return res;
}

function reverseArrayInPlace(x){
    for(let i = 0; i < Math.floor(x.length/2); i++){
        let temp = null;
        temp = x[i]; 
        x[i] = x[x.length-1-i];
        x[x.length-1-i] = temp;
    }
}

reverseArray([6, 7, 45, 6]);

let toRev = [1, 234, 56, 12, 0, -6];
reverseArrayInPlace(toRev);
