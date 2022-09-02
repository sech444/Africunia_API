import rsa
import uuid

# Use at least 2048 bit keys nowadays, see e.g. https://www.keylength.com/en/4/
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

plaintext = "0xc0d8e04cb6cdba67db7cda88b5f054117f7327c3187a46baa72ca9a82707ec40".encode('utf8')
#print("Plaintext: ", plaintext)

ciphertext = rsa.encrypt(plaintext, publicKeyReloaded)
#print("Ciphertext: ", ciphertext)
 
decryptedMessage = rsa.decrypt(ciphertext, privateKey)
#print("Decrypted message: ", decryptedMessage)


def generateUUID():
    user_id = uuid.uuid5(uuid.NAMESPACE_DNS, "publicKeyPkcs1PEM")
    #s = shortuuid.encode(user_id)
    #short = s[:6]
    print(user_id)
    return user_id#str(short)

with open("decryptedMessage", "r") as file:
    Compiled_code = file.read()
    print(Compiled_code)






