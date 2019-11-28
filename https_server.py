from aiohttp import web
import ssl

async def handle(request):
    name = request.match_info.get('name', "world ~")
    text = "Hello, " + name
    return web.Response(text=text)


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])

    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain("./server/server.crt", "./server/server.key")
    ssl_context.load_verify_locations("./ca/ca.crt")
    ssl_context.verify_mode = ssl.CERT_REQUIRED

    web.run_app(app,host='127.0.0.1',port=5000, ssl_context=ssl_context)

