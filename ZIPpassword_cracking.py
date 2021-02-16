#dictionary attack
import zipfile
from threading import Thread

#zfile과 사전에서 선택한 패스워드를 인자로 받아 해당 ZIP파일의 압축 해제를 시도하고 성공하면 압축해제와 함께 패스워드를 화면에 출력
def crackzip(zfile, passwd):
    try:
        zfile.extractall(pwd=passwd)
        print("ZIP file extacted successfully! PASS=[%s]" %passwd.decode())
        return True
    except:
        pass
    return False

def main():
    dictfile = 'dictionary.txt' #사전파일
    zipfilename = 'locked.zip'  #패스워드가 걸린 zip file
    zfile = zipfile.ZipFile(zipfilename, 'r')
    pfile = open(dictfile, 'r')

    for line in pfile.readlines():
        passwd = line.strip("\n")
        t = Thread(target=crackzip, args=(zfile, passwd.encode('utf-8')))
        t.start()

if __name__ == '__main__':
    main()