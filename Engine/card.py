#####################################
# Author : Rahul Raikwar            #
# Description :                     #
#                                   #
# The following code will encrypt   #
# and decrypt the card details of   #
# the user.                         #
#####################################

from Crypto.Cipher import AES
from Crypto import Random
import json
import binascii


class Card:
    def __init__(self, key, details=""):
        self.details = details
        self.iv = Random.new().read(AES.block_size)
        self.key = key
        self.aes_obj = AES.new(self.key, AES.MODE_CFB, self.iv)

    def strip(self, string):
        _str = string
        _x = 0
        for x in _str:
            if (x == '"'):
                break
            else:
                _x += 1
        return _x

    @property
    def encrypt_data(self):
        _en_data = self.iv + self.aes_obj.encrypt(
            json.dumps(self.details).encode("utf-8"))
        return binascii.hexlify(_en_data).decode('utf-8').strip()

    def decrypt_data(self, ciphertext):
        ciphertext = ciphertext.encode('utf-8')
        ciphertext = binascii.unhexlify(ciphertext)
        data = self.aes_obj.decrypt(ciphertext).decode('ISO-8859-1')
        offset = self.strip(data)

        return data[offset:]


if __name__ == '__main__':

    key = "7195bb5b30deff29d83ac5n2b50b8c68"
    details = {
        'aadhaarno': '234-2788-98987',
        'name': 'mohd shibli',
        'dob': '27-09-1997',
        "address": "kathmandu",
        'email': 'mohdshitbit@kamfakd.com'
    }
    card = Card(key.encode("utf-8"), str(details))
    # print(card)
    cipher = "53efd37873e384a846aea88270afd6a5c57a6a2c175a6d480113ad5b293e5d79729e2b5b900a0cf611eebce0b151d64804d6314abb39ae887b51e939aa02cf4bb85f373400c18deb2d14cbe52ce3ba13f7c7d5a5eca5c5e7270e07c2c0f64f225fcae13792d3030a0dbb05415a13f6602981f6381691c9cc8eca34c1610bb1d920a88177"

    # size of the ciphertext in kb
    # print(len(cipher) / 1024)
    print(cipher)
    print("-------------------------------------------")
    print(Card(key.encode("utf-8")).decrypt_data(cipher))
