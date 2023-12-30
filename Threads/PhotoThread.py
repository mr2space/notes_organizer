from uuid import uuid4
import joblib
import os
import threading
import shutil
from TextRecognition import ImageToTextAPI, ImagePreProcessing, TextClean


class PhotoThread(threading.Thread):
    def __init__(self, photo_path: str, cache_path= str(os.getcwd())+r"\Images\cache") -> None:
        threading.Thread.__init__(self)
        self.cache_path = cache_path
        self.photo_path = photo_path
        self.y = -1

    def return_pickleClass(self, path):
        return joblib.load(path)

    def run(self):
        photo_path = self.photo_path
        cache_path = self.cache_path
        temp_folder = str(uuid4())
        ImageEngine = ImagePreProcessing.ImagePreProcessingClass(photo_path)
        ImageEngine.gray_scaling()
        os.mkdir(cache_path + f"\\{temp_folder}")
        ImageEngine.split_save_img(cache_path + f"\\{temp_folder}")
        number = ImageEngine.number
        del ImageEngine
        TextEngine = ImageToTextAPI.ImageToText()
        text_data = ''
        for i in range(number):
            filename = cache_path + f"\\{temp_folder}" + f"\\temp_{i}.png"
            text_data += " " + TextEngine.recognize(filename)
        text_cleaner = TextClean.TextClean(text_data)
        text_data = " ".join(text_cleaner.text)
        model = self.return_pickleClass(r"SvmModel/model.joblib")
        vector = self.return_pickleClass(r"SvmModel/vector.joblib")
        text_data = vector.transform([text_data])
        self.y = model.predict(text_data)
        return self.y[0][0]

