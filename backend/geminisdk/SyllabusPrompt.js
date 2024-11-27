import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager } from "@google/generative-ai/server";
import { configDotenv } from "dotenv";
configDotenv("..");
import { promp } from "./prompt.js";

const genAi = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const fileManager = new GoogleAIFileManager(process.env.GEMINI_API_KEY);

const model = genAi.getGenerativeModel({ model: "gemini-1.5-flash" });

const SyllabusPrompt = async (filePath) => {
  const uploadResponse = await fileManager.uploadFile(filePath, {
    mimeType: "application/pdf",
    displayName: "Gemini 1.5 PDF",
  });
  const result = await model.generateContent([
    {
      fileData: {
        mimeType: uploadResponse.file.mimeType,
        fileUri: uploadResponse.file.uri,
      },
    },
    { text: promp.syllabus },
  ]);

  let cleanedString = result.response
    .text()
    .replace(/```json/g, "") // Remove '''json
    .replace(/```/g, "") // Remove '''
    .replace(/\n/g, "");
  console.log(cleanedString)
  let jsonObject = JSON.parse(cleanedString);
  return jsonObject;
};

export default SyllabusPrompt;
