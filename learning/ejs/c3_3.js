function countBs(x){
    return countChar(x, "B");
}

function countChar(x, ch){
    let chCount = 0;
    for(let c of x){
        if(c == ch){
            chCount += 1;
        }
    }
    return chCount;
}

console.log(countBs("BarBBBBBboo"));
console.log(countChar("reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaet", "a"));
console.log();
