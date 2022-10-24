
    ## Part of iq.opengenus.org
import codecs
import ecdsa
import secrets
import hashlib

# generate bitcoin private key
def generate_private_key():
    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    return bits_hex[2:]

private_key = "60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2"

 # return 64-byte key, 2 32-byte representing x,y coordinates of elliptic curve
def generate_public_key():
    # private_key = generate_private_key()
    priv_key_bytes = codecs.decode(private_key, 'hex') # convert string into byte array
    key = ecdsa.SigningKey.from_string(priv_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    public_key = codecs.encode(key_bytes, 'hex')
    return public_key 

public_key = generate_public_key()
print("Generated Public Key: ", public_key.decode())
print()

def convert_pub_key(public_key):
    bit_public_key = b'0x04' + public_key
    return bit_public_key.decode()[2:]

bit_pub_key = convert_pub_key(public_key)
print("Standard Bitcoin Pub_Key: ", bit_pub_key)
print()

# compress public key
def compress_pub_key(public_key):
    mid = int(len(public_key) / 2)
    x = public_key[:mid]
    if(int(public_key[-1:]) % 2 == 0):
        x = b'0x02' + x
    else:
        x = b'0x03' + x
    return x

compressed_pub_key = compress_pub_key(public_key)

print("Compressed Pub_Key: ", compressed_pub_key.decode()[2:])
print()

# Encrypt public key
def encrypt_pub_key(compressed_pub_key):
    public_key = compressed_pub_key.decode()[2:]
    public_key_bytes = codecs.decode(public_key, 'hex')
    sha256_pub_key = hashlib.sha256(public_key_bytes) # pass public key through SHA-256
    sha256_pub_key_digest = sha256_pub_key.digest()
    ripemd160_pub_key = hashlib.new('ripemd160') # pass hashed SHA-256 through RIPEMD
    ripemd160_pub_key.update(sha256_pub_key_digest)
    ripemd160_pub_key_digest = ripemd160_pub_key.digest()
    ripemd160_pub_key_hex = codecs.encode(ripemd160_pub_key_digest, 'hex')
    return ripemd160_pub_key_hex

encrypted_pub_key = encrypt_pub_key(compressed_pub_key)
print("Encrypted Pub_Key:", encrypted_pub_key.decode())
print()

# adding network byte
def network_byte(encrypted_pub_key, network):
    if(network == 'mainnet'):
        return b'0x00' + encrypted_pub_key
    elif(network == 'testnet'):
        return b'0x6f' + encrypted_pub_key
    else:
        print('Invalid Network')

net_pubkey = network_byte(encrypted_pub_key, 'mainnet')
print("Bitcoin mainnet Addr: ", net_pubkey.decode()[2:])
print()

# calculate checksum of address
def calc_addr_checksum(net_pubkey):
    sha256_net_pubkey = hashlib.sha256(net_pubkey) # first SHA
    sha256_net_pubkey_digest = sha256_net_pubkey.digest()
    sha256_2_sha256_net_pubkey = hashlib.sha256(sha256_net_pubkey_digest) # second SHA
    sha256_2_net_pubkey_digest = sha256_2_sha256_net_pubkey.digest()
    sha256_2_hex = codecs.encode(sha256_2_net_pubkey_digest, 'hex')
    checksum = sha256_2_hex[:8]
    return checksum

checksum = calc_addr_checksum(net_pubkey)
print("Checksum: ", checksum.decode())
print()

# create wallet address
def wallet_address(public_key, checksum):
    # checksum = b'512f43c4'
    return public_key + checksum

wallet_addr = wallet_address(net_pubkey, checksum)
print("Wallet Address: ", wallet_addr.decode()[2:])
print()

# Ecnode with Base58 encoding
def base58(address_hex):
    address_hex = wallet_addr.decode()[2:]
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_string = ''
    # Get the number of leading zeros
    leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
    # Convert hex to decimal
    address_int = int(address_hex, 16)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add '1' for each 2 leading zeros
    ones = leading_zeros // 2
    for _ in range(ones):
        b58_string = '1' + b58_string
    return b58_string

Bit_wallet_addr = base58(wallet_addr)

print("Final Bitcoin Wallet Address: ", Bit_wallet_addr)
print()
private_key_bytes = codecs.decode(str(private_key, hex))
# Get ECDSA public key
key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
key_bytes = key.to_string()
key_hex = codecs.encode(key_bytes, hex)