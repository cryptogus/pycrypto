from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA #해시함수를 이용해 3DES의 암호키와 초기화 벡터를 만들 때 활용하기 위함 

def make85tring(msg): # 임의의 메세지 블록크기에 맞게 패딩
    msglen = len(msg)
    filler = ""
    if msglen%8 != 0:
        filler = "0"*(8 - msglen % 8)
    msg += filler
    return msg

class myDES():
    #__init__() - 클래스 생성인자, keytext - 암호키 생성 문자열, ivtext - 초기화 벡터
    def __init__(self, keytext, ivtext):
        #keytext의 크기가 16바이트면 3DES의 키로 바로 사용가능하지만 16자 이상이면 외우기 힘듬
        #따라서 keytext의 길이가 무었이든 SHA256 해시를 이용하면 일정 크기로 키 사용가능
        hash = SHA.new()
        hash.update(keytext.encode("utf-8"))#해시갱신, 단 update()는 유니코드 문자열을 인자로 받지 못함
        #따라서 utf-8로 인코딩한 keytext문자열을 입력
        key = hash.digest()#해시값을 key변수에 저장(32byte)
        self.key = key[:24]#3DES의 키 크기는 16 or 24byte이기때문에 처음 24byte로 슬라이싱

        hash.update(ivtext.encode("utf-8"))
        iv = hash.digest()
        self.iv = iv[:8]#3DES는 64비트 암호블록이기 때문에 CBC모드의 iv값은 8바이트크기가 되어야함

    def enc(self, plaintext):
        plaintext = make85tring(plaintext)#패딩
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)#인자는 순서대로 암호키,운용모드,초기화벡터
        encmsg = des3.encrypt(plaintext)
        return encmsg

    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decmsg = des3.decrypt(ciphertext)
        #패딩제거함수 필요
        return decmsg

def main():
    keytext = "samsjang"
    ivtext = "1234"
    msg = "python35"

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)
    print("ORIGINAL:\t%s" %msg)
    print("CIPHERED:\t%s" %ciphered)
    print("DECIPHERED:\t%s" %deciphered)

if __name__ == "__main__":
    main()