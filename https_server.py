from flask import Flask
import ssl
import asyncio

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'




if __name__ == '__main__':
    CA_FILE = "./ca/ca.crt"
    KEY_FILE = "./server/server.key"
    CERT_FILE = "./server/server.crt"
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_REQUIRED

    #app.run(debug=True, ssl_context=context)
    server = app.run(debug=True, ssl_context=context)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(server)
    loop.run_forever()

    #app.run(debug=True, ssl_context=context)

