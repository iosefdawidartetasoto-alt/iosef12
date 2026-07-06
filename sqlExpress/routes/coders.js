const express = require("express");
const router = express.Router()
const db = require("../db")

/**
 * @swagger
 * /coders:
 *   get:
 *     summary: Retrieve a list of users
 *     description: Fetches a predefined list of dummy users from the server.
 *     tags:
 *       - Coders
 *     responses:
 *       201:
 *          description: creado exitosamente.
 *       500:
 *         description: Internal server error.
 */
router.get("/", async(request, response)=>{
    const result = await db.query("SELECT * FROM coders");

    response.json(result.rows)
})

/**
 * @swagger
 * /coders:
 *   post:
 *     summary: Crear un usuario
 *     tags:
 *       - Coders
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               fullname:
 *                 type: string
 *                 required: true
 *               email:
 *                 type: string
 *                 format: email
 *                 required: true
 *               birthdate:
 *                 type: string
 *                 format: date
 *                 required: true
 *               identification:
 *                 type: string
 *                 required: true
 *               clan:
 *                 type: string
 *                 required: true
 *                 enum: ["Micaela", "Mulata", "Magdalena", "Garabato"]
 *     responses:
 *       201:
 *         description: Usuario creado
 * 
 */
router.post("/", async(request, response)=>{
    const {fullname, birthdate, email, identification, clan} = request.body;
    const result = await db.query(
        "INSERT INTO coders(fullname, birthdate, email, identification, clan) values($1, $2, $3, $4, $5) RETURNING *",
        [fullname, birthdate, email, identification, clan]
    );
    response.status(201).json(result.rows[0])
})

module.exports = router
