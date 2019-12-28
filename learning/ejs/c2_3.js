let x, y = 1;
let size = 8;
for(let x=1; x<=size; x+=1){
    let row = ""
    for(let y=1; y<=size; y+=1){
        if((x+y) % 2 == 1){
            row += ("#");
        }
        else{
            row += ("  ");
        }
    }
    console.log(row);
}
