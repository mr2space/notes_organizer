import requests
import os
import shutil
from dotenv import load_dotenv

load_dotenv(r".env")

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')

class ImageToText:
    __API_URL = API_URL
    __headers = {"Authorization": API_KEY}


    def recognize(self, filename):
        # print(filename)
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(self.__API_URL, headers=self.__headers, data=data, json={"wait_for_model": True})
        print(response)
        return self.return_text(response.json())

    def return_text(self, data):
        print(data)
        return data[0].get("generated_text", "")

