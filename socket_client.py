import socket, asyncio
import ssl


async def echo_client():
    # 向服务端发送信息
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.check_hostname = False
    context.load_cert_chain(certfile="./client/client.crt", keyfile="./client/client.key")
    context.load_verify_locations("./ca/ca.crt")
    context.verify_mode = ssl.CERT_REQUIRED

    sock = socket.socket()
    ssock = context.wrap_socket(sock, server_side=False)
    ssock.connect(('127.0.0.1', 5678))
    msg = "do i connect with server ?".encode("utf-8")
    ssock.send(msg)
    # 接收服务端返回的信息
    msg = ssock.recv(1024).decode("utf-8")
    print(f"receive msg from server : {msg}")
    ssock.close()



if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(echo_client())
    event_loop.close()
