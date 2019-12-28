function factorize(n){
    let factors = [];
    for(let i = 1; i <= n; i++){
        if(i in factors || n/i in factors){continue}
        else{
            if(n%i == 0){
                factors.push(i)
                factors.push(n/i)
            }
        }
        //console.log(i)
    }
    return factors
}
function antiprimes(n){ // All antiprimes less than n
    let mostFactors = 0;
    let bestAntiprime = 0;
    for(let i = 1; i <= n; i++){
        factors = factorize(i).length;
        if(factors > mostFactors){
            mostFactors = factors;
            bestAntiprime = i;
        }
    }
    return bestAntiprime;
}
/*function primes(n){
    let primes = [];
    for (let i = 1; i <= n; i++){
        if(factorize(i).length == 2){
            primes.push(i)
        }
    }
    return primes
}*/

function primes(lwr=1, n){
    let primes = [];
    for (let i = lwr; i <= n; i++){
        if(factorize(i).length == 2){
            primes.push(i)
        }
    }
    return primes
}
console.log(antiprimes(500));
console.log(primes(50));
//console.log(primes(50,300));
