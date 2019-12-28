const syllable = require("syllable");
const fs = require("fs");

text = fs.readFile("kjv.txt", function(err, data){
    var text = String(data);
    text = String(text.split("*** START OF THIS PROJECT GUTENBERG EBOOK THE KING JAMES BIBLE ***")[1]);
    text = String(text.split("End of the Project Gutenberg EBook of The King James Bible")[0]);
    text = text.split("\n\n");
    text.forEach(function(x){
        x = x.split(" ")
        x = x.slice(1)
         x
    });
    //console.log(text)
    let lines = []
    text.forEach(function(x){
        if(x != ""){
            lines.push(x);
        } 
    });
    for (line in lines){
        lines[line] = lines[line].replace(/\n$/, "");
    }
    console.log(lines);
})