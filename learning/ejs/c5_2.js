function loop(val, test, update, body){
    for(let i = val; test(i); i = update(i)){
        body(i);
    }
}

loop(5, x => x < 10, i => i+1, x => {console.log(x);});
