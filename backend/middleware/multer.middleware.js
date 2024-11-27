import multer from "multer";
import fs from "fs";

const storage = multer.diskStorage({
    destination:(req, file, cb) => {
        cb(null, "upload/")
    },
    fileFilter: (req, file, cb) =>{
        cb(null,true);
    },
    filename:(req, file, cb)=>{
        cb(null, Date.now() + "-" + file.originalname);
    },
})

export const singleCleanUp = (path, time = 60) => {
    setTimeout(() => {
        fs.unlink(path, (err) => {
          if (err) {
            console.error('Error deleting the file:', err);
            // return res.status(500).send('Error deleting the file');
          }
          console.log('File deleted after 10 seconds');
        //   res.send('File uploaded and deleted after delay');
        });
      }, 1000 * time);  // 10 seconds delay before cleanup
}
export const upload = multer({ storage: storage });