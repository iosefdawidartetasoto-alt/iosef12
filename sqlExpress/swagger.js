
const swaggerJsDoc = require("swagger-jsdoc");

const options = {
    definition:{
        openapi: "3.0.0",
        info: {
            title: "CRUD de Coders",
            version: "1.0.0",
            description: "Esta es mi primera API, construida por mí, sin ayuda de IA, jajaja soy el mejor"
        },
        servers:[
            {
                url: "http://localhost:3002"
            }
        ]
    },
    apis: ["./routes/*.js"]
}

module.exports = swaggerJsDoc(options)