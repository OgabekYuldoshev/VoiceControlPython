const http = require("http")
const express = require("express")
const app = express()
const data = require("./DataBase/iakt.json")
const server = http.createServer(app)

app.use(express.static("public"))

app.get("/iakt", (req, res)=>{
  res.json(data)
})

server.listen(8080 || process.env.PORT , ()=>{
  console.log("Port Running")
})
