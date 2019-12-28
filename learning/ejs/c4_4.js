function deepEqual(x, y){
    // What I missed:
    // a === b
    // if either is null or not object, return false
    // length check
    if(x === y) return true;
    if(x === null || y === null || typeof x !== "object" || typeof y !== "object"){
        return false;
    }
    xKeys = Object.keys(x);
    yKeys = Object.keys(y);
    if(xKeys.length != yKeys.length) return false;
    for(let k of xKeys){
            for(let l of yKeys){
               /* if(typeof x[k] == "object" && x[k] !== null){
                    return deepEqual(x[k], y[k]);
                }
                else{
                    if(x[k] !== y[k]){
                        return false;
                     };
                 }*/ 
                if(k === l){
                    if(typeof x[k] == "object" && x[k] !== null && typeof y[l] == "object" && y[l] !== null){
                        return deepEqual(x[k], y[l])
                    }
                    else{
                        if(x[k] !== y[l]){
                            return false
                        }
                    }
                }
             }
    }
    return true;
}

let sampleObject = {hi: "roo", "ghee": {"roo": 678}};
let sampleObject2 = {hi: "roo", "ghee": {"roo": 16000}, butter: {"me": 9, yoo: 900, us: "reet"}};

console.log(deepEqual(sampleObject, sampleObject2));
