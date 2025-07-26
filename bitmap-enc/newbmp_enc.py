from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PIL import Image
import binascii, os, random, struct


def convert2RGB(data):
    r, g, b = tuple(
        map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2])
    )
    pixels = tuple(zip(r, g, b))
    return pixels


def encrypt_bmp_file(key, mode, iv, in_filename, out_filename=None):
    im = Image.open(in_filename)
    data = im.convert("RGB").tobytes()
    original = len(data)

    # PKCS7 Padding
    pad_len = 16 - len(data) % 16
    pad = pad_len.to_bytes(1, byteorder="big", signed=False) * pad_len
    data += pad

    # Encryption by given mode (cryptography)
    if mode == "ECB":
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    elif mode == "CBC":
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    else:
        raise ValueError("Unsupported mode")
    encryptor = cipher.encryptor()
    encrypted_bytes = encryptor.update(data) + encryptor.finalize()
    encrypted = convert2RGB(encrypted_bytes[:original])

    im2 = Image.new(im.mode, im.size)
    im2.putdata(encrypted)
    im2.save(out_filename)
    print(f"{in_filename} is encrypted.")


key = bytes.fromhex("43454E4143454E4143454E4143454E41")
iv = bytes.fromhex("43454E4143454E4143454E4143454E41")


str1 = "x.bmp"
str2 = str1 + ".ecb.bmp"
str3 = str2 + ".bmp"
encrypt_bmp_file(key, "ECB", iv, str1, out_filename=str2)
# decrypt_bmp_file(key, 'ECB', iv, str2, out_filename = str3)
str2 = str1 + ".cbc.bmp"
str3 = str2 + ".bmp"
encrypt_bmp_file(key, "CBC", iv, str1, out_filename=str2)
# decrypt_bmp_file(key, 'CBC', iv, str2, out_filename = str3)
