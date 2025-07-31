import requests
import base64
from nacl.public import SealedBox, PublicKey
from nacl.encoding import Base64Encoder

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
REPO = "YOUR_USERNAME/GARA"
SECRET_NAME = "GARA_SERVER_URL"
public_url = "YOUR_NGROK_URL" 

# fetch public key
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}
key_url = f"https://api.github.com/repos/{REPO}/actions/secrets/public-key"
res = requests.get(key_url, headers=headers)
key_data = res.json()
key_id = key_data["key"]
key_id_val = key_data["key_id"]

# encrypt
pk = PublicKey(key_id.encode("utf-8"), encoder=Base64Encoder)
box = SealedBox(pk)
encrypted = base64.b64encode(box.encrypt(public_url.encode())).decode()

# upload
payload = {
    "encrypted_value": encrypted,
    "key_id": key_id_val
}
put_url = f"https://api.github.com/repos/{REPO}/actions/secrets/{SECRET_NAME}"
res = requests.put(put_url, headers=headers, json=payload)
print(res.status_code)