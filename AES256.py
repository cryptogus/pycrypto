from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    # print(plaintext.encode('utf-8'))
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

def decrypt(ciphertext, key):
    nonce = ciphertext[:16]
    tag = ciphertext[16:32]
    ciphertext = ciphertext[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

# Generate a random 256-bit (32-byte) key
key = get_random_bytes(32)

# Example usage
message = "Hello, World!"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)