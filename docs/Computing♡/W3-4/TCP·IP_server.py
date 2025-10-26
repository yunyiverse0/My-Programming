 # 서버 프로그램 (server.py)

# 내 컴퓨터를 서버로 만든 뒤, 외부에서 접속할 수 있도록 포트(정해진 포)를 여는 파이썬 코드


import socket  # 네트워크 통신을 위한 소켓 불러

# 서버 IP 및 포트 설정
server_ip = '0.0.0.0'  # 0.0.0.0 -> 모든 IP로부터 접근 허용 (127.0.0.1 -> 내 컴퓨터만 가능)
server_port = 12345    #서버가 열어둘 포트 번호 (0 ~ 65535)

# TCP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))  # IP와 포트 연결

server_socket.listen(1)  # 연결 대기
print(f"서버가 준비되었습니다: IP={server_ip}, PORT={server_port}")

# 클라이언트의 접속을 기다림
client_socket, client_addr = server_socket.accept()
print(f"클라이언트 접속: {client_addr}")

# 클라이언트 메시지 수신
data = client_socket.recv(1024)
print(f"받은 메시지: {data.decode()}")

# 응답 보내기
client_socket.sendall("서버가 메시지를 받았습니다.".encode("UTF-8"))

# 연결 종료
client_socket.close()
server_socket.close()



##############################서버 계속 열어두는 코드



import socket
import sys

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

server_ip = '127.0.0.1'
server_port = 50000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"서버가 준비되었습니다: IP={server_ip}, PORT={server_port}")

while True:
    client_socket, client_addr = server_socket.accept()
    print(f"클라이언트 접속: {client_addr}")

    data = client_socket.recv(1024)
    if not data:
        break
    print(f"받은 메시지: {data.decode()}")

    client_socket.sendall("서버가 메시지를 받았습니다.".encode("utf-8"))
    client_socket.close()  # 클라이언트 연결만 닫기

