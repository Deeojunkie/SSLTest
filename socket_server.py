import socket
import asyncio
import ssl


async def handle_echo(client, addr):
    msg = client.recv(1024).decode('utf8')
    print(f"receive msg from client {addr}：{msg}")
    response = f"yes , you have client_socketect with server.\r\n"
    client.send(response.encode('utf8'))
    client.close()


async def run_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="./server/server.crt", keyfile="./server/server.key")
    context.load_verify_locations("./ca/ca.crt")
    context.verify_mode = ssl.CERT_REQUIRED

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    # 将socket打包成SSL socket
    server = context.wrap_socket(sock, server_side=True)
    server.bind(('127.0.0.1', 5678))
    server.listen(5)
    server.setblocking(False)

    while True:
        client, addr = await loop.sock_accept(server)
        loop.create_task(handle_echo(client, addr))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_server())
    loop.close()


