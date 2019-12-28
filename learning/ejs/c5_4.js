const SCRIPTS = require("./scripts.js");

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



function writingDirection(c){
    return characterScript(c.codePointAt(0)).writingDirection;
}

console.log(writingDirection("a"));
