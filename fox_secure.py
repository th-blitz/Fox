import hashlib
import secrets
import base64
import base58
import gzip
import ecdsa
import json
import sys
import time

def sha3_256(data):
    hash = hashlib.sha3_256(data.encode('utf-8')).hexdigest()
    return hash

def sha3_512(data):
    hash = hashlib.sha3_512(data.encode('utf-8')).hexdigest()
    return hash

def shake_256(data, digest_in_bytes):
    hash = hashlib.shake_256(data.encode('utf-8')).hexdigest(digest_in_bytes)
    return hash

def shake_128(data, digest_in_bytes):
    hash = hashlib.shake_128(data.encode('utf-8')).hexdigest(digest_in_bytes)
    return hash

def sha256(data):
    hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hash

def sha512(data):
    hash = hashlib.sha512(data.encode('utf-8')).hexdigest()
    return hash

def generate_random_bits(bit_length = 256):
    bits = secrets.randbits(256)
    return bits

def generate_fox_private_key(key_length = 256):

    bits = generate_random_bits(bit_length = key_length)
    bits = str(hex(bits))
    bits = bits[2:]
    fox_private_key = bits
    return fox_private_key

def select_ecdsa_curve(fox_private_key, curve = 'SECP256k1'):
    if curve == 'SECP256k1':
        curve = ecdsa.SECP256k1
    ecdsa_curve = ecdsa.SigningKey.from_string( bytearray.fromhex(fox_private_key), curve=curve)
    return ecdsa_curve

def generate_fox_public_key(fox_private_key, ecdsa_curve):

    public_key = ecdsa_curve.verifying_key
    public_key = public_key.to_string("compressed").hex()
    fox_public_key = public_key
    return  fox_public_key

def get_checksum(data, digest_in_bytes):
    checksum = sha3_256(data)
    checksum = shake_128(checksum, digest_in_bytes)
    return checksum

def hexbase58(key):

    if isinstance(key, str):
        try:
            intnum = int(key, 16)
            type = 'hex'
        except ValueError:
            type = 'b58'
            pass

        if type == 'hex':
            address = base58.b58encode_int(intnum).decode('utf-8')
        elif type == 'b58':
            address = base58.b58decode_int(key)
            address = hex(address)
        else:
            address = None

    elif isinstance(key, int):
        address = base58.b58decode_int(key).decode('utf-8')

    return address


def generate_fox_public_address(github_url, fox_public_key, ecdsa_curve):

    github_url = github_url.split('//')[1]

    dict = {
        'info' : {
            'public_key': fox_public_key , 'github_url': github_url
        },
        'info_hash' : '',
        'info_signature' : ''
    }
    dict_info = dict['info']['github_url'] + '||' + dict['info']['public_key']
    sha3_512_dict = sha3_512(dict_info)
    shake_256_dict = shake_256(sha3_512_dict, 20)
    checksum = get_checksum(shake_256_dict, 4)
    address = 'f0' + shake_256_dict + checksum
    address_base58 = hexbase58(address)
    github_url = dict['info']['github_url']
    dict = ( github_url + '_' + address_base58)
    fox_public_address = 'fox_' + dict

    return fox_public_address

def decode_fox_public_address(fox_public_address):

    github_url = fox_public_address.split('_')[1]
    address = fox_public_address.split('_')[2]
    address = hexbase58(address)
    checksum = address[-8:]
    address = address[4:-8]

    address = hex(int(address, 16))[2:]

    if len(address) < 40:
        first_zeros = 40 - len(address)
        for i in range(first_zeros):
            address = '0' + address
    else:
        first_zeros = 0

    check = get_checksum(address, 4)
    if check == checksum:
        checksum = True
    else:
        checksum = False

    return  github_url, 'f0' + address, checksum, first_zeros

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

def fox_address_generator(github_url , curve = 'SECP256k1', strength = None):

    if strength == None:
        for i in range(100):

            try:
                key = generate_fox_private_key()
                ecd_curve = select_ecdsa_curve(key, curve)
                break
            except:
                continue

        public_key = generate_fox_public_key(fox_private_key = key, ecdsa_curve = ecd_curve)
        public_address = generate_fox_public_address(github_url , fox_public_key = public_key, ecdsa_curve = ecd_curve)

    elif isinstance(strength, int):

        i = 0
        count = 0
        animation = r"/-\|/"
        time_out = 120.0
        before = time.time()

        while(True):

            key, public_key, public_address = fox_address_generator(github_url, curve)
            url, address, checksum, temp_strength = decode_fox_public_address(public_address)
            count += 1

            if count % 1000 == 0:

                sys.stdout.write("\r" + f"[...{animation[i % len(animation)]}] going through hashes = {count}")
                sys.stdout.flush()
                i += 1

            now = time.time()

            if temp_strength >= strength:
                print(" - done")
                print(f'- Time taken : {int(now - before)}s')
                break

            elif (now - before) > time_out:
                print(f" --->> time out {time_out} seconds")
                print(f'- Time taken : {int(now - before)}s')
                break


    return key , public_key , public_address
