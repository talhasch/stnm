from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from stnm.web.app import app

PORT = 5000
ADDRESS = "127.0.0.1"


def callback():
    print("Server running at http://{}:{}".format(ADDRESS, PORT))


def web():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(PORT, address=ADDRESS)
    IOLoop.instance().add_callback(callback)
    IOLoop.instance().start()
