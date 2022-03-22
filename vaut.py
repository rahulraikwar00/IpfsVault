import os
import sys
import json
import requests
from Engine import card as cardX, user as userX
import cryptography


class Valut:
    def __init__(self) -> None:
        self.key = ""
        self.aadharno = ""
        # create a json file and return file object if not exist
        if not os.path.exists("data.json"):
            with open("data.json", "w") as f:
                json.dump([], f)

    # encrypt the data and return the ciphertext
    def encryptfile(self, details: dict):
        card = cardX.Card(self.key.encode("utf-8"), str(details))
        cipher = card.encrypt_data
        return cipher

    # decrypt the data and return the plaintext
    def decryptfile(self, details: str):
        return cardX.Card(self.key.encode("utf-8")).decrypt_data(details)

    def upload(self, details: dict):
        # encrypt the details
        cipher = self.encryptfile(details)
        files = {details["aadhaarno"]: cipher}
        response = requests.post("http://127.0.0.1:5001/api/v0/add", files=files)
        p = response.json()
        # hash = p["Hash"]
        print(p)

        return True

    def download(self, aadhaarno: str):
        with open("data.json", "r") as f:
            data = json.load(f)
            self.aadharno = data[0][aadhaarno]

        params = (("arg", hash),)
        response_two = requests.post(
            "http://127.0.0.1:5001/api/v0/block/get", params=params
        )
        print(response_two.text)
        with open("data.json", "r") as f:
            data = json.load(f)
        if aadhaarno in data:
            return self.decryptfile(data[aadhaarno])
        else:
            return False

    def setkey(self, key: str):
        self.key = key
        return True


obj = Valut()
obj.key = "7195bb5b30deff29d83ac5n2b50b8c68"
obj.upload(
    {
        "aadhaarno": "334-788-98188",
        "name": "mohd shibli",
        "dob": "27-09-1997",
        "address": "kathmandu",
        "email": ")",
    }
)
