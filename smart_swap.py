import rsa
import uuid
import json
import shortuuid

from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA
from Cryptodome.PublicKey import RSA
from base64 import b64decode
"""# Use at least 2048 bit keys nowadays, see e.g. https://www.keylength.com/en/4/
publicKey, privateKey = rsa.newkeys(2048) 

# Export public key in PKCS#1 format, PEM encoded 
publicKeyPkcs1PEM = publicKey.save_pkcs1().decode('utf8') 
#print(publicKeyPkcs1PEM)
# Export private key in PKCS#1 format, PEM encoded 
privateKeyPkcs1PEM = privateKey.save_pkcs1().decode('utf8') 
#print(privateKeyPkcs1PEM)

# Save and load the PEM encoded keys as you like

# Import public key in PKCS#1 format, PEM encoded 
publicKeyReloaded = rsa.PublicKey.load_pkcs1(publicKeyPkcs1PEM.encode('utf8')) 
# Import private key in PKCS#1 format, PEM encoded 
privateKey = rsa.PrivateKey.load_pkcs1(privateKeyPkcs1PEM.encode('utf8')) 

#plaintext = "".encode('utf8')
#print("Plaintext: ", plaintext)

#ciphertext = rsa.encrypt(plaintext, publicKeyReloaded)
#print("Ciphertext: ", ciphertext)
 
#decryptedMessage = rsa.decrypt(ciphertext, privateKey)
#print("Decrypted message: ", decryptedMessage)


def generateUUID():
    user_id = uuid.uuid5(uuid.NAMESPACE_DNS, publicKeyPkcs1PEM)
    #s = shortuuid.encode(user_id)
    #short = s[:6]
    print(user_id)
    return user_id#str(short)

generateUUID()

with open("decryptedMessage", "r") as file:
    Compiled_code = file.read()
    #print(Compiled_code)
    
with open("base_1.pem", "r") as file:
    ciphertext = file.read()
    print(ciphertext)
 
rsa_key = Crypto.IO.PEM.decode('base_1.pem', "rb")
print(rsa_key)
print(" .....................")   
privateKeyPkcs1PEM = to_bytes(ciphertext, 'big')
publicKeyReloaded = rsa.PublicKey.load_pkcs1(publicKeyPkcs1PEM.encode('utf8'))
decryptedMessage = rsa.decrypt(ciphertext, privateKey)
print("Decrypted message: ", decryptedMessage)









def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

generate_keys()
pubKey, privKey = load_keys()

message = input('Enter a message:')
ciphertext = encrypt(message, pubKey)

signature = sign_sha1(message, privKey)

plaintext = decrypt(ciphertext, privKey)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')

if plaintext:
    print(f'Plain text: {plaintext}')
else:
    print('Could not decrypt the message.')

if verify_sha1(plaintext, signature, pubKey):
    print('Signature verified!')
else:
    print('Could not verify the message signature.')
"""
def generateUUID():
    user_id = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    print(user_id)
    decoded_uuid = uuid.decode(user_id)
    print(decoded_uuid)
    s = shortuuid.encode(user_id)
    short = s[:6]
    h = shortuuid.decode(short)
    print(h)
    return str(short)
print(generateUUID())