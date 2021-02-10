#RSA 1024
#Code for generating and storing private keys
#개인키가 있으면 공개키는 다시 생성가능, rsa프로그램을 이용시 개인키가 소멸되는 것을 막기 위한 저장프로그램
from Crypto.PublicKey import RSA

def createPEM():
    private_key = RSA.generate(1024)
    f = open("mykey.pem", 'wb+')
    f.write(private_key.exportKey("PEM"))
    f.close()
    #mykey.pem이라는 파일이 생성됨

if __name__ == '__main__':
    createPEM()