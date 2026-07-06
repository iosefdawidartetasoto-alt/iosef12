require("dotenv").config();
const swaggerUI = require("swagger-ui-express")
const swaggerSpec = require("./swagger")
console.log(process.env.PORT);

const express = require("express")

const app = express()

app.use(express.json())

app.use(
  "/api-docs",
  swaggerUI.serve,
  swaggerUI.setup(swaggerSpec)
)


app.use("/coders", require("./routes/coders"))

const port = process.env.PORT || 3001

app.listen(port, () => {
  console.log(`Servidor ejecutándose en http://localhost:${port}`);
});