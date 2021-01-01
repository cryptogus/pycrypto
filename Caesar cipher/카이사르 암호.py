#참고도서 - 화이트 해커를 위한 암호와 해킹

ENC = 0
DEC = 1 #전역변수

def makeDisk(key): #key는 알파벳 문자 1개
    #keytable은 (알파벳 문자, 문자 인덱스) 튜플이 멤버인 리스트 [('A',0),('B',1)....]
    #chr은 아스키코드를 입력받아 유니코드(아스키문자)로 반환, chr(x+65)은 x가 0~25이기때문에 A~Z반환, chr(65) = A
    keytable = map(lambda x:(chr(x+65), x), range(26))
    #lambda 인자,인자,.. : 식 ex) f = lambda x: x*x -> f(2) = 4 출력
    #map(함수, 반복 가능한)
    #keytable을 이용해 {알파벳 문자:문자 인덱스}인 사전자료
    key2index = {}
    for t in keytable:
        alphabet, index = t[0], t[1]
        key2index[alphabet] = index

    if key in key2index:
        k = key2index[key]
    else:
        return None, None

    #enc_disk - 키는 평문 문자 : 임호문 문자 사전
    #dec_disk - 키는 암호문 문자 : 평문 문자 사전
    #만약 암호키가 B(1)라면 암호문 문자는 순서대로 B,C,D... 만약 F(5)라면 F,G,H...
    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (i+k)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)

    return enc_disk, dec_disk

def caesar(msg, key, mode):
    ret = ''#빈 문자열 선언

    msg = msg.upper() # msg의 모든 문자를 대문자로 변경
    enc_disk, dec_disk = makeDisk(key)

    if enc_disk is None:
        return ret

    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]#A~Z까지가 수행됨
        else:
            ret += c #숫자 EX)007 -> 007그대로 암호화됨
        return ret

def main():
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = 'F'
    #%s는 포맷 문자열
    print("Original:\t%s" %plaintext.upper())
    ciphertext = caesar(plaintext, key ,ENC)
    print("caesar cipehr:\t%s" %ciphertext)
    decipehrtext = caesar(ciphertext, key ,DEC)
    print("Deciphered:\t%s" %decipehrtext)

if __name__=='__main__':
    main()