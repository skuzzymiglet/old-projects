kl = "rett";


    function arrayToList(x){
    let list = null;
    for(let i = x.length-1; i >= 0; i--){
        list = {value: x[i], rest: list};
    }
    return list;
}

console.log(arrayToList([0, 2, 3]));

