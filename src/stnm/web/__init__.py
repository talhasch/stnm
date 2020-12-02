from aparat import env_vars
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from stnm.web.app import app

PORT = env_vars("WEB_PORT") or 8081
ADDRESS = env_vars("WEB_ADDRESS") or "127.0.0.1"


def callback():
    print("-" * 40)
    print("Server running at {}:{}".format(ADDRESS, PORT))
    print("Web UI (not ready) http://{}:{}/ui".format(ADDRESS, PORT))
    print("API http://{}:{}/api".format(ADDRESS, PORT))
    print("-" * 40)


def web():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(PORT, address=ADDRESS)
    IOLoop.instance().add_callback(callback)
    IOLoop.instance().start()
