from pprint import pprint
import re
import os
import time
import json
import requests
from Engine import card as cardX, keygen as keygenX


class Valut:
    def __init__(self, masterkey=None) -> None:
        self.masterkey = masterkey
        self.aadharno = ""
        self.encodefile = ""
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
    def decryptfile(self, datastring: str):
        print(len(datastring))
        card = cardX.Card(self.key.encode("utf-8")).decrypt_data(datastring)
        print(card)
        return True

    def upload(self, details: dict):
        # encrypt the details
        cipher = self.encryptfile(details)
        files = {details["aadhaarno"]: cipher}
        response = requests.post("http://127.0.0.1:5001/api/v0/add", files=files)
        p = response.json()
        # hash = p["Hash"]
        # print(p)

        return p

    def download(self, hash: str):

        params = (("arg", hash),)
        response_two = requests.post(
            "http://127.0.0.1:5001/api/v0/block/get", params=params
        )
        return response_two.text

    def setkey(self, key: str):
        self.key = key
        return True


obj = Valut()
obj.key = "7195bb5b30deff29d83ac5n2b50b8c68"
raw_data = {
    "aadhaarno": "333-788-98188",
    "name": "Rahul Raikwar",
    "dob": "27-09-2000",
    "address": "New york ",
    "email": "rr200636@gmail.com",
}
data = obj.upload(raw_data)


pprint(raw_data)
pprint("Encryption is in process... wait!")
time.sleep(2)
pprint("Uploding to IPFS ...")
time.sleep(1)
pprint("\n--------------------------------------------------------")
pprint("Done !")
pprint(data)
sdata = obj.download(data["Hash"])
sdata = sdata.rstrip(sdata[-1])

sdata = re.sub("[^a-z0-9]+", "", sdata, flags=re.IGNORECASE)
print(sdata)
print("Decryption The data.....wait!")
time.sleep(1)
pprint("done!")
obj.decryptfile(sdata)
