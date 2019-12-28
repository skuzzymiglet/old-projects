function every(array, test){
    for(let e of array){
        if(!test(e)){
            return false
        }
    }
    return true;
}

let ones = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];
let oddies =[5, 345, 345, 1, 1, 1, 1, 1,1,1,1,1,1,1,6,4,6];

console.log(every(oddies, i=>i<400));
