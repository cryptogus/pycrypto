#지정된 파일의 내용을 읽고 암호화가능
#암호화, 복호화 파일의 확장자 txt로 바꿔주어야함
from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA

from os import path   #파일크기를 리턴하는 함수 getsize()를 이용하기 위함
KSIZE = 1024 #전역변수 선언

class myDES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode("utf-8"))
        key = hash.digest()
        self.key = key[:24]

        hash.update(ivtext.encode("utf-8"))
        iv = hash.digest()
        self.iv = iv[:8]

#filename으로 지정된 파일 크기를 구하고,파일 크기가 8바이트 배수가 아닐 경우 8바이트 배수가 되게 0문자열을 패딩
    def makeEncInfo(self, filename): 
        fillersize = 0
        filesize = path.getsize(filename)
        if filesize % 8 != 0:
            fillersize = 8 - filesize % 8
        filler = '0'*fillersize
        header = '%d' %(fillersize)  #추가할 문자개수
        gap = 8-len(header)
        header += "#"*gap
        
        return header, filler
#filename 으로 지정된 파일 내용을 1KB씩 읽어서 3DES로 암호화후 새로운 파일에 저장
    def enc(self, filename):
        encfilename = filename + ".enc" #원래 파일 이름에 .enc확장자를 추가하여 만듬
        header, filler = self.makeEncInfo(filename)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)

        h = open(filename, "rb")
        hh = open(encfilename, 'wb+')
        enc = header.encode("utf-8")#유니코드
        content = h.read(KSIZE) #파일에서 1KB만큼 읽어서 content에 담음
        content = enc + content
        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')
            enc = des3.encrypt(content)
            hh.write(enc)
            content = h.read(KSIZE)
        h.close()
        hh.close()
#encfilename으로 지정된 암호화된 파일 내용을 1KB씩 읽어서 3DES로 복호화
    def dec(self, encfilename):
        filename = encfilename + ".dec" #복호화 된 내용은 dec 확장자 파일에 저장
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)

        h = open(filename, 'wb+')
        hh = open(encfilename, 'rb')

        content = hh.read(8) #암호화 파일의 최초 8바이트를 읽어 3DES로 복호화
        dec = des3.decrypt(content)
        header = dec.decode()
        fillersize = int(header.split('#')[0]) # '#'을 구분자로 헤더를 분리한 후 첫 번째 맴버를 정수로 변환하면 이 파일의 끝부분에 추가된 문자'0'의 개수를 얻음

        content = hh.read(KSIZE) #암호화파일에서 1KB를 먼저 읽고 content에 담은후 반복문으로 진입
        while content:
            dec = des3.decrypt(content)
            if len(dec) < KSIZE:
                if fillersize != 0:
                    dec = dec[:-fillersize] #암호화때 추가한 "0"문자열 제거
            h.write(dec)
            content = hh.read(KSIZE)
        h.close()
        hh.close()

def main():
    keytext = "hyenholee"
    ivtext = '1234'
    filename = 'plain.txt'
    encfilename = filename + ".enc" #복호화 사용

    myCipehr = myDES(keytext, ivtext)
    myCipehr.enc(filename)
    myCipehr.dec(encfilename) #복호화 사용

if __name__ == '__main__':
    main()
    
        

