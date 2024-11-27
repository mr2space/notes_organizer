import express, { Router } from "express";

import { upload } from "../middleware/index.js";
import {syllabusUploadController} from "../controllers/index.js";

const router = Router();

router.post(
  "/syllabus",
  upload.single("file"),
  syllabusUploadController
);

export default router;
