#codebook암호
#특정 문자를 특정한 문자로 치환하여 만드는 암호
#참고 도서 - 화이트 해커를 위한 암호와 해킹
def makeCodebook():
    decbook = {"5":"a","2":"b","#":"d","8":"e","1":"f","3":"g","4":"h","6":"i","0":"i","9":"m","*":"n",
    "%":"o","=":"p","(":"r",")":"s",",":"t","?":"u","@":"v",":":"y","7":" "}

    encbook={}
    for k in decbook:
        val = decbook[k]
        encbook[val] = k
    
    return encbook, decbook

def encrypt(msg, encbook): #암호화를 위한 함수
    for c in msg:
        if c in encbook:
            msg = msg.replace(c,encbook[c])

    return msg

def decrypt(msg,decbook): #복호화를 위한 함수
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])

    return msg

if __name__ == '__main__' : #c언어의 main함수 같은 역할. 프로그램의 시작점. c언어와의 차이점 - main함수가 다른 파일에 여러개 존재가능
    
    h = open('plain.txt','rt') # plain.txt 를 텍스트 읽기 모드로 열고, 읽은 내용을 모두 변수 content에 저장 - plain.txt파일 필요
    #open( )에서 rt - 텍스트 읽기 모드로 파일 오픈, rb - 바이너리 읽기 모드, wt - 텍스트 쓰기 모드로 파일 오픈, wb - 바이너리 쓰기 모드 
    content = h.read()#read - 파일에 있는 모든 내용을 문자열로 리턴

    h.close()#open함수를 통해 파일객체를 얻었으면 파일처리 후 반드시 닫아줘야함

    encbook, decbook = makeCodebook()
    content = encrypt(content, encbook)
    
    h = open('encyption.txt','wt+')#encryption.txt 텍스트쓰기 모드로 열고 암호화된 내용을 파일에 기록 - 파일이 존재하지 않으니 생성됨
    #wt+ - 텍스트쓰기모드로 파일을 오픈, wb+ -바이너리
    h.write(content) #write - 인자로 입력된 문자열을 파일에 기록(문자열만 입력)
    h.close
    # 복호화는 비슷하게 하면 된다
    # deciphertext = decrypt(ciphertext, decbook)
    # print('복호문 = ', deciphertext)