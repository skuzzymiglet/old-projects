let i = 0;

for(let i = 1; i <= 100; i++){
    let text = ""; 
    if (i%3 == 0){
        text += ("Fizz");
    }
    if (i%5 == 0){
        text += ("Buzz");
    }
    if(text==""){
        text = String(i)
    }
    console.log(text);
}
