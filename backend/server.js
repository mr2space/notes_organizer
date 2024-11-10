import express from "express";

import { configDotenv } from "dotenv";
import { mlogger } from "./middleware/index.js";
import Urlrouter from "./routes/index.js";

configDotenv()
const app = express();


//logger
app.use(mlogger)

// All routes
app.use("", Urlrouter);


app.listen(process.env.PORT, () => {
    console.log(`server running ... ${ process.env.PORT }`);
});