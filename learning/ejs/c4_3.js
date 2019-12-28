function arrayToList(x){
    let list = null;
    for(let i = x.length-1; i >= 0; i--){
        list = {value: x[i], rest: list};
    }
    return list;
}

function listToArray(x){
    let sub = x;
    let array = [];
    while(sub !== null){
        array.push(sub.value);
        sub = sub.rest;
    }
    return array
}

function prepend(value, list){ 
    return {value, rest: list};
}

function nth(list, index){
    if(index == 0){
        return list.value;
    }
    else if(index > 0){
        return undefined;
    }
    else{
        return nth(list.rest, index-1);
    }
}

console.log(arrayToList([1, 67, 345]));
console.log(prepend(456, arrayToList([1, 67, 345])));
console.log(nth(arrayToList([1, 45, 6, 8, 2]), 78));
