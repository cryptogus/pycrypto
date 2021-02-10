#RSA_private.py create "mykey.pem"
#It uses a private key created with RSA_private.py
from Crypto.PublicKey import RSA

def readPEM(): #"mykey.pem"파일에 저장된 개인키를 읽어서 리턴함
    h = open("mykey.pem", "r")
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_enc(msg): #공개키로 암호화
    private_key = readPEM()
    public_key = private_key.publickey()
    encdata = public_key.encrypt(msg, 32)
    return encdata

def rsa_dec(msg):  #개인키로 복호화
    private_key = readPEM()
    decdata = private_key.decrypt(msg)
    return decdata

if __name__ == "__main__":
    msg = "samsar love python"
    ciphered = rsa_enc(msg.encode("utf-8"))
    print(ciphered)
    deciphered = rsa_dec(ciphered)
    print(deciphered)