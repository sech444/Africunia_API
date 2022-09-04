from cryptography.fernet import Fernet
message = '0xc0d8e04cb6cdba67db7cda88b5f054117f7327c3187a46baa72ca9a82707ec40'

key = Fernet.generate_key()
print(key)
fernet_obj = Fernet(key)
encrypted_message = fernet_obj.encrypt(message.encode())
print(encrypted_message)
decrypted_message = fernet_obj.decrypt(encrypted_message).decode()
print("massage", decrypted_message)
print(len(b'wWmkM1l-qiPDHXMg6W0P9uciZj6h79LBBATsB9FF6Wo='))
encrypted_message = b'gAAAAABjFHIBYqHqxUMNO2NVGzKybsP2qvAHhULut2K_DbmhgIU1zBchfpdthCSP88dlMGfBPev4xn6KBtw9X8s15T08Ya694Qfrbwr4-g9yTbFC5qUt6Kgjm5V83c-IGyd91TMhbTG-mfhszR7m6Kqk1u0KQSIkCrdC2Jg37dwq8QoII9VWGRQ='