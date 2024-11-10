import express, { Router } from "express";

import {upload} from "../middleware/index.js";
import {singleNotesUpload} from "../controllers/index.js";

const router = Router();

router.post(
  "/photo-single",
  upload.single("file"),
  singleNotesUpload
);

export default router;
