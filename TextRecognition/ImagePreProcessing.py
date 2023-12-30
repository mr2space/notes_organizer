from PIL import Image
import cv2 as cv
import os


class ImagePreProcessingClass:
    __img = None

    number = 1

    def __delete_files(self, path):
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                os.remove(os.path.join(path, filename))

    def split_save_img(self, path):
        image_parts = []
        height, width = self.__img.shape
        ratio = 5 * (height // 1000) + 1
        self.number = ratio
        start_h = 0
        h_ratio = height // ratio

        while h_ratio <= height:
            part = self.__img[start_h:h_ratio, :]
            temp = h_ratio
            h_ratio += h_ratio - start_h
            start_h = temp
            image_parts.append(part)
        try:
            self.__delete_files(path)
        except:
            pass
        for idx, img_part in enumerate(image_parts):
            try:
                temp = Image.fromarray(img_part)
                temp.save(rf'{path}\temp_{idx}.png')
            except Exception as e:
                print("Error at save", e)
                break

    def __init__(self, filename) -> None:
        self.__img = cv.imread(filename)

    def gray_scaling(self):
        self.__img = cv.cvtColor(self.__img, cv.COLOR_BGR2GRAY)
        self.__img = cv.medianBlur(self.__img, 5)
        self.__img = cv.GaussianBlur(self.__img, (5, 5), 2)
        self.__img = cv.adaptiveThreshold(self.__img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 2)