import os

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from stnm.web.app import app

PORT = os.environ.get("WEB_PORT") or 8081
HOST = os.environ.get("WEB_HOST") or "127.0.0.1"


def callback():
    print("-" * 40)
    print("Server running at {}:{}".format(HOST, PORT))
    print("STNM API http://{}:{}/api".format(HOST, PORT))
    print("Mining Bot Web UI http://{}:{}/ui".format(HOST, PORT))
    print("-" * 40)


def web():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(PORT, address=HOST)
    IOLoop.instance().add_callback(callback)

    try:
        IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nBye")
