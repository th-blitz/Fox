import hashlib
import secrets
import base64
import gzip
import ecdsa
import json

def generate_random_bits(bit_length = 256):
    bits = secrets.randbits(256)
    return bits

def generate_fox_private_key(key_length = 256):

    bits = generate_random_bits(bit_length = key_length)
    bits = str(hex(bits))
    bits = bits[2:]
    fox_private_key = 'f0'+ bits[2:]

    return fox_private_key

def select_ecdsa_curve(fox_private_key, curve = 'SECP256k1'):
    if curve == 'SECP256k1':
        curve = ecdsa.SECP256k1
    ecdsa_curve = ecdsa.SigningKey.from_string( bytearray.fromhex(fox_private_key), curve=curve)
    return ecdsa_curve

def generate_fox_public_key(fox_private_key, ecdsa_curve):

    public_key = ecdsa_curve.verifying_key
    public_key = public_key.to_string("compressed").hex()
    fox_public_key = 'fox_' + public_key
    return  fox_public_key

def generate_fox_public_address(github_url, fox_public_key, ecdsa_curve):

    github_url = github_url.split('//')[1]

    dict = {
        'info' : {
            'public_key': fox_public_key , 'github_url': github_url
        },
        'info_hash' : '',
        'info_signature' : ''
    }
    dict_info = dict['info']['public_key'] + '||' + dict['info']['github_url']
    dict_info = dict_info.encode('utf-8')
    sha3_512_dict = hashlib.sha3_512(dict_info).hexdigest()
    sha3_512_dict = sha3_512_dict.encode('utf-8')
    sha3_256_dict = hashlib.sha3_256(sha3_512_dict).hexdigest()
    shake_256_dict = hashlib.shake_256(sha3_256_dict.encode('utf-8')).hexdigest(16)

    checksum = hashlib.sha3_256(shake_256_dict.encode('utf-8')).hexdigest()
    checksum = hashlib.shake_128(checksum.encode('utf-8')).hexdigest(4)
    print(shake_256_dict)
    print(checksum)
    address = shake_256_dict + checksum
    print(address)
    address_base64 = base64.b64encode(address.encode('utf-8')).decode('utf-8')
    github_url_base64 = base64.b64encode(dict['info']['github_url'].encode('utf-8')).decode('utf-8')
    dict = ( github_url_base64 + '_' + address_base64)
    fox_public_address = 'fox_' + dict

    return fox_public_address

def decode_fox_public_address(fox_public_address):

    github_url_base64 = fox_public_address.split('_')[1]
    checksum = fox_public_address.split('_')[2]
    github_url = base64.b64decode(github_url_base64).decode('utf-8')

    return  github_url, checksum

def verify_signature(fox_public_key, signature, data_hash, curve = 'SECP256k1'):

    public_key = fox_public_key.split('_')[1]
    signature = base64.b64decode(signature)
    if curve == 'SECP256k1':
        curve = ecdsa.SECP256k1
    vk = ecdsa.VerifyingKey.from_string( bytearray.fromhex(public_key) , curve=curve)
    try:
        ans = vk.verify(signature, data_hash.encode('utf-8'))
    except ecdsa.keys.BadSignatureError:
        ans = False

    return ans

key = generate_fox_private_key()
curve = 'SECP256k1'
ecd_curve = select_ecdsa_curve(key, curve)
public_key = generate_fox_public_key(fox_private_key = key, ecdsa_curve = ecd_curve)
github_url = r'https://github.com/ThBlitz'
public_address = generate_fox_public_address(github_url , fox_public_key = public_key, ecdsa_curve = ecd_curve)
print(public_address)
url, checksum = decode_fox_public_address(public_address)
print(url, checksum)
