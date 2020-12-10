from Crypto.Cipher import AES
from PIL import Image
import binascii, os, random, struct

def convert2RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data))if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r,g,b))
    return pixels

def encrypt_bmp_file(key, mode, iv, in_filename, out_filename = None):
    # Get RGB data from BMP file
    im = Image.open(in_filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    
    # PKCS7 Padding
    pad_len = 16 - len(data) % 16
    pad = pad_len.to_bytes(1, byteorder='big', signed = False) * pad_len
    data += pad

# Encryption by given mode
    encryptor = AES.new(key, mode, iv)
    encrypted = convert2RGB(encryptor.encrypt(data)[:original])

# Create a new PIL Image object and
# save the old image data into the new image.
im2 = Image.new(im.mode, im.size)
im2.putdata(encrypted)

# Save image
im2.save(out_filename)
print ("{} is encrypted.".format(in_filename))
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

for j in range(0,9):
    mode = AES.MODE_ECB
    str1 = "sample_{:02d}.bmp".format(j)
    str2 = str1 + ".ecb.bmp"
    str3 = str2 + ".bmp"
    encrypt_bmp_file(key, mode, iv, str1, out_filename = str2)
    #decrypt_bmp_file(key, mode, iv, str2, out_filename = str3)

    mode = AES.MODE_CBC
    str1 = "sample_{:02d}.bmp".format(j)
    str2 = str1 + ".cbc.bmp"
    str3 = str2 + ".bmp"
    encrypt_bmp_file(key, mode, iv, str1, out_filename = str2)
    #decrypt_bmp_file(key, mode, iv, str2, out_filename = str3)