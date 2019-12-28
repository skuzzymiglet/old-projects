const syllable = require("syllable");
const fs = require("fs");

text = fs.readFile("kjvdat.txt", function(err, data){
    var text = String(data);
    var lines = text.split("\n");
    let verses = [];
    lines.forEach(function(x){
        verses.push(x.split("|")[3]);
    });
    let clauses = [];
    verses.forEach(function(x){
        clauses.push(x.split(/.,?!;~/));
    });
    console.log(clauses);
})