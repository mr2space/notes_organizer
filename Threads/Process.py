import os
from Threads.PhotoThread import PhotoThread
import shutil

class Process:
    def __init__(self, path) -> None:
        self.path = path
        files = []
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                files.append(filename)
        self.files = files
    def start(self):
        if not self.files:
            print("Folder is empty")
            return -1
        photo_map = {}
        threadlist = []
        for photo in self.files:
            t = PhotoThread(self.path + f"\\{photo}")
            threadlist.append(t)
            t.start()
        for t, photos in zip(threadlist, self.files):
            t.join()
            photo_map[photos] = t.y
        self.photo_map = photo_map
        self.create_folder()

    def create_folder(self):
        for photo in self.photo_map:
            try:
                os.mkdir(self.path + f"\\{self.photo_map[photo][0]}")
            except:
                pass
            os.rename(self.path + f"\\{photo}", self.path + f"\\{self.photo_map[photo][0]}" + f"\\{photo}")

