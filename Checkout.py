import json
import base64
import hashlib
from Crypto.Cipher import AES

class Checkout(object):

    def __init__(self, key, iv_):
        self.byte_string = 16
        self.key = hashlib.sha256(key.encode()).hexdigest()[:32]
        self.iv = hashlib.sha256(iv_.encode()).hexdigest()[:16]

    def encrypt(self, raw):
        """
        Encrypt passed json data with the secret key,iv key.
        """
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, self.iv.encode('utf-8'))
        crypt = cipher.encrypt(self._pad(raw).encode())
        return base64.b64encode(base64.b64encode(crypt)).decode('utf-8')

    def _pad(self, s):
        return s + (self.byte_string - len(s) % self.byte_string) * chr(self.byte_string - len(s) % self.byte_string)

payload = json.dumps({
    "merchantTransactionID":"1558439939759",
    "customerFirstName":"John",
    "customerLastName":"Doe",
    "MSISDN":"2547XXXXXXXX",
    "customerEmail":"john.doe@example.com",
    "requestAmount":"100",
    "currencyCode":"KES",
    "accountNumber":"10092019",
    "serviceCode":"MULADEMOX",
    "dueDate":"2019-06-01 23:59:59",
    "requestDescription":"Dummy merchant transaction",
    "countryCode":"KE",
    "languageCode":"EN",
    "successRedirectUrl":"<YOUR_SUCCESS_REDIRECT_URL>",
    "failRedirectUrl":"<YOUR_FAIL_REDIRECT_URL>",
    "paymentWebhookUrl":"<PAYMENT_WEBHOOK_URL>"
})

print(Checkout('1234567890', 'qwertyuiop').encrypt(payload))

