let stack = ["5+8", "9*6", "return 67 == 65+2"];
stack.push("console.log(67)");
for(let el of stack){
    let f = new Function("", stack.pop())
    console.log(f());
    console.log();
    console.log(stack);
}
