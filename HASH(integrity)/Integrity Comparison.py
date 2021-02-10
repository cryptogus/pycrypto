#두 파일의 무결성을 해시함수로 비교하는 코드
# 충돌쌍일 확률은 고려 안한듯 보임
from Crypto.Hash import SHA256 as SHA
SIZE = 1024*256

def getFileHash(filename):
    hash = SHA.new()
    h = open(filename, 'rb')
    content = h.read(SIZE)
    while content:
        hash.update(content)
        hashval = hash.digest()
        content = h.read(SIZE)
    h.close()
    return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)
    if hashval1 == hashval2:
        print("Two Files are Same")
    else:
        print("Two Files are Different")

def main():
    file1 = 'plain.txt'
    file2 = 'plain2.txt'
    hashCheck(file1, file2)

if __name__ == '__main__':
    main()
