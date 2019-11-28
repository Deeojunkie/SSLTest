import urllib.request
import asyncio
import ssl

async def client():

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.check_hostname = False
    context.load_cert_chain(certfile="./client/client.crt", keyfile="./client/client.key")
    context.load_verify_locations("./ca/ca.crt")
    context.verify_mode = ssl.CERT_REQUIRED
    try:
        # 通过request()方法创建一个请求：
        request = urllib.request.Request('https://127.0.0.1:5000/')
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


if __name__ == '__main__':
    asyncio.run(client())

