import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

client_address = '/tmp/udp_client_socket_file'



try:
    os.unlink(client_address)
except FileNotFoundError:
    pass
sock.bind(client_address)

try:
    while True:
        print('メッセージを入力してください。終了するには"exit"と入力してください。')
        message = input()


        print(f"送信メッセージ：{message}")
        sent = sock.sendto(message.encode(), server_address)
        if message.strip().lower() == 'exit':
            break

        print('応答を待っています。')

        data, server = sock.recvfrom(4096)

        print('{!r}を受け取りました。'.format(data.decode()))

finally:
    print('ソケットを閉じます。')
    sock.close()
    if os.path.exists(client_address):
        os.unlink(client_address)