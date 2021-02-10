from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

def readPEM():
    h = open("mykey.pem", 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

#사용자의 개인키로 서명하는
def rsa_sign(msg):
    private_key = readPEM()
    public_key = private_key.publickey()
    hash = SHA.new(msg).digest()
    signature = private_key.sign(hash, '')
    return public_key, signature

#사용자의 공개키로 서명을 확인하는 측
def rsa_verify(msg, public_key, signature):
    hash = SHA.new(msg).digest()
    if public_key.verify(hash, signature):
        print("VERIFIED")
    else:
        print("DENIED")

if __name__ == '__main__':
    msg = "I love you"
    public_key, signature = rsa_sign(msg.encode("utf-8"))
    rsa_verify(msg.encode("utf-8"),public_key, signature)