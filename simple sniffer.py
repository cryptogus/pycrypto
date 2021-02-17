from socket import *
import os #코드가 실행되는 컴퓨터의 OS종류를 확인을 위해 os.name을 사용하기 위함

#sniffing함수는 Raw 소켓을 생성한 뒤 인자로 입력된 host와 바인드하고 소켓옵션으로 IP 헤더를 포함하여 수신할거라 설정
#호스트로 전송되는 모든 네트워크 패킷을 수신하기 위해 promiscuous 모드로 변경
def sniffing(host):
    if os.name == 'nt': #윈도우인 경우(윈도우는 프로토콜에 관계없이 들어오는 모든 패킷을 가로채기 때문에 IP를 지정해도 무관)
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP #유닉스 or 리눅스는 ICMP를 가로채겠다는 것을 명시해야함

    sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))
    sniffer.setspckopt(TPPROTO_IP, IP_HDRINCL, 1)

    if os.name =='nt':
        sniffer.ioctl(SIO_RCVALL, RCVALL_ON)
    packet = sniffer.recvfrom(65565)# 65565는 버퍼의 크기 즉 65565바이트
    print(packet)

    if os.name == 'nt':
        sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)

def main():
    host = gethostbyname(gethostname()) #getgostbyname() 은 호스트 이름을 IPv4형식으로 바꿈, 현재 호스트의 이름을 리턴
    print("START SNIFFING at [%s]" %host) #host에는 컴퓨터의 IP주소가 담김
    sniffing(host)
#윈도우의 경우 윈도우 커맨드 창을 관리자 권한으로 실행하여 이 파일을 파이썬 명령으로 구동하면 됨
if __name__ == '__main__':
    main()
