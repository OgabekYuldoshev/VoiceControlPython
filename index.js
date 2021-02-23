const express = require("express")
const app = express()
const data = require("./DataBase/iakt.json")

app.get("/", (req, res)=>{
  res.sendFile(__dirname + "/index.html")
})
app.get("/iakt", (req, res)=>{
  res.json(data)
})

app.listen(8080 || process.env.PORT, ()=>{
  console.log("Port Running")
})