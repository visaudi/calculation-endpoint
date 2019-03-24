const fs = require("fs");
const express = require("express");
const app = express();
const port = 3000;

app.get("/", function (request, response) {
    const {spawn} = require("child_process");
    const python = spawn("python", ["amplyoptim1.py"]);

    python.on("close", function (code) {
        fs.readFile("./current.json", "utf-8", function(error, json) {
            response.json(JSON.parse(json));
        });
    });
});

app.listen(port, () => console.log(`App listening on port ${port}!`));
