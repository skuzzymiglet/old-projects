const SCRIPTS = require("./scripts.js");

function repeat(n, action){
    for(let i = 0; i < n; i++){
        action(i);
    }
}

function appender(x){
    return (s) => {return s += x};
}

function minArgs(f, sampleArgs){
    let args = [];
    console
    for(let i = 0; i <= sampleArgs.length-1; i++){
        args.push(sampleArgs[i]);
        result = f(...args);
        console.log(n, args, result);
        if(result !== undefined){
            return i
        }
    }
    return Infinity;
}

function callAndDebug(f, args){
    console.log("function:", f);
    console.log("args:", args);
    console.log("calling");
    f(...args);
    console.log("calling and storing");
    result = f(...args);
    console.log("returned", result);
}

//repeat(5, (n) => {console.log(`RASTA PAI NAMBA ${n+1}`)});
function repeatString(x, n){
    let result = "";
    for(let i = 0; i <= n-1; i++){
        result += x;
    }
    return result;
}

let newScripts = SCRIPTS.sort((a, b) => {return a.year - b.year});
let longestName = SCRIPTS.reduce((a, b) => {return (a.name.length < b.name.length ? b : a)}).name.length;

//console.log(longestName, repeatString("#", longestName))

//for(let script of newScripts){
  //  console.log(script.name, repeatString(" ", longestName + 1 - script.name.length), Math.floor(script.year/100));
//}

newScripts = newScripts.filter(s => s.living).map(x => ({century: Math.floor(x.year/10), name: x.name, year: x.year}))

//console.log(newScripts[0], newScripts[newScripts.length - 1]);
if(false){
    for(let i = newScripts[0].century; i <= newScripts[newScripts.length - 1].century; i++){
        //console.log("yearz");
        let currentScripts = newScripts.filter(x => {return x.century == i});
        if(currentScripts.length == 0){
            console.log("|");
        }
        else{
            currentScripts.forEach(x => console.log(x.name, x.year));
        }
    }
}

let isPrintable = /^[^\p{Cc}\p{Cf}\p{Zl}\p{Zp}]*$/;
if(false){
    for(let script of SCRIPTS){
        let sample = "";
        script.ranges.forEach(x => x.forEach(y => {if(isPrintable.test(String.fromCodePoint(y))){ sample += String.fromCodePoint(y)}}));
        console.log(script.name, sample);
    }
}

if(false){
    for(let i = 0; i <= 500; i++){
        if(isPrintable.test)
        console.log(String.fromCodePoint(i));
    }
}

function countBy(items, groupName) {
  let counts = [];
  for (let item of items) {
    let name = groupName(item);
    let known = counts.findIndex(c => c.name == name);
    if (known == -1) {
      counts.push({name, count: 1});
    } else {
      counts[known].count++;
    }
  }
  return counts;
}

console.log(countBy([1, 2, 3, 4, 5], n => n > 2));
// → [{name: false, count: 2}, {name: true, count: 3}]

//console.log(SCRIPTS);

function characterScript(code) {
  for (let script of SCRIPTS) {
    if (script.ranges.some(([from, to]) => {
      return code >= from && code < to;
    })) {
      return script;
    }
  }
  return null;
}

function inScript(c, scriptName){
    return characterScript(c.codePointAt(0)).name == scriptName;
}


//console.log(countBy(SCRIPTS, x => x.year).sort((a, b) => a.count - b.count));
console.log(characterScript(568));

function textScripts(text){
    let scripts = countBy(text, char => {
        let script = characterScript(char.codePointAt(0));
        return script ? script.name : "none";
    }).filter(({name}) => name != "none")

    let total = scripts.reduce((n, {count}) => n + count, 0);
    if(total == 0) return "No scripts, bitch";

    return scripts.map(({name, count}) => {
        return `${Math.round(count * 100 / total)}% ${name}`;
    }).join(", ")
}

console.log(textScripts("yarik, baloo英国的狗, мат; матерщи́на / ма́терный язы́к / мáтный язы́к"))
