/* web/app.js
 * Ian Kollipara
 * 2020.11.22
 * Express Server App
 */

// Imports
const express = require("express");
const path = require("path");

const app = express();

app.use(express.static(path.join(__dirname, "build")));

app.get("/*", (req, res) => {
  res.sendFile(path.join(__dirname, "build", "index.html"));
});

app.listen(3000);
