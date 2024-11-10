import express, { Router } from "express"

import UploadRouter from "./upload.route.js";

const router = Router();

router.use("/upload",UploadRouter);


export default router;