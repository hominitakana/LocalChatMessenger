import socket
import os
from faker import Faker

# ソケットの作成
# UNIXドメインソケットを使用
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/udp_socket_file'

# Fakerオブジェクトの作成
fake = Faker()

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass

print('{}を起動します。'.format(server_address))
sock.bind(server_address)

try:
    while True:
        #クライアントからのメッセージを受信し出力
        print('\nメッセージを待っています。')
        data, address = sock.recvfrom(4096)

        print('{}から{}バイト受け取りました。'.format(address, len(data)))
        print('受信データ：{}'.format(data.decode()))
        
        # ランダムな文字列を生成しクライアントに送信
        if data:
            if data.decode().strip().lower() == 'exit':
                print('サーバーを終了します。')
                break

            else:
                random_text = fake.lexify(text = "????????")
                message = f"ランダムな文字列：{random_text}"
                print('応答メッセージ：{}'.format(message))
                sock.sendto(message.encode(), address)

finally:
    print('ソケットを閉じます。')
    sock.close()
    if os.path.exists(server_address):
        os.unlink(server_address)