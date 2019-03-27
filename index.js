const fs = require("fs");
const express = require("express");
const app = express();
const port = 3000;

let n = 24;
let j = 0;
console.log(j);
/*for (let j = 0; j <= n; j++) {
    
    
        
}*/

setInterval(function(){
    if (j <= n){
        j = j +1;
        console.log(j);
        
    };
},2000)

        app.get("/", function (request, response) {
        const {spawn} = require("child_process");
        const python = spawn("python", ["amplyoptim1.py",j]); 
        python.on("close", function (code) {
        fs.readFile("./current.json", "utf-8", function(error, json) {
            response.json(JSON.parse(json));
        });
    });
});

/*setInterval(function(){
    if (j <= n){
        j = j +1;
        console.log(j);
        app.get("/", function (request, response) {
        const {spawn} = require("child_process");
        const python = spawn("python", ["amplyoptim1.py","j"]);
        console.log(j);
        python.on("close", function (code) {
        fs.readFile("./current.json", "utf-8", function(error, json) {
            response.json(JSON.parse(json));
        });
    });
});
    }
},2000)*/



/*let current_sample = 0;

setInterval(function(){
    if (current_sample <= 24){
        current_sample += 0.5;
    }
},2000)
*/

/*app.get("/", function (request, response) {
    const {spawn} = require("child_process");
    const python = spawn("python", ["amplyoptim1.py","1"]);

    python.on("close", function (code) {
        fs.readFile("./current.json", "utf-8", function(error, json) {
            response.json(JSON.parse(json));
        });
    });
});
*/

/*app.get("/current-time", function (request, response) {
    const {spawn} = require("child_process");
    const python = spawn("python", ["amplyoptim1.py","20",current_sample]);

    python.on("close", function (code) {
        fs.readFile("./current.json", "utf-8", function(error, json) {
            response.json(JSON.parse(json));
        });
    });
});
*/

app.listen(port, () => console.log(`App listening on port ${port}!`));
