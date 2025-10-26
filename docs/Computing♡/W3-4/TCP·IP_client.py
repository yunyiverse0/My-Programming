import socket

server_ip = '127.0.0.1'  # 서버(내 컴퓨터)
server_port = 8080

# TCP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))  # 서버에 접속

# 메시지 보내기
client_socket.sendall("안녕 ㅎ".encode("UTF-8"))

# 서버로부터 응답 수신
data = client_socket.recv(1024)
print("서버 응답:", data.decode())

# 연결 종료
client_socket.close()
