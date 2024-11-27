import { asyncHandler } from "../utils/asynchandler.js";
import ApiResponse from "../utils/ApiResponse.js";
import { singleCleanUp } from "../middleware/multer.middleware.js";

import { SyllabusGemini } from "../geminisdk/index.js";

export const syllabusUploadController = asyncHandler(async(req, res)=>{
    // url : "/upload/photo-single"
    console.log("file path", req.file);
    const result = await SyllabusGemini(req.file.path);
    singleCleanUp(req.file.path);
    return res.json(new ApiResponse(
        200,
        {
            msg:"wo evers",
            "response":result
        }
    ))
})