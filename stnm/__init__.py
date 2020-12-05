import os
import sys

from stnm.config import config
from stnm.config import get_config_path
from stnm.constants import DEFAULT_CONFIG
from stnm.install import install
from stnm.response import error_response
from stnm.shell import which
from stnm.start import start
from stnm.status import status
from stnm.stop import stop
from stnm.test import do_tests
from stnm.web import web


def main(cmd: str, arg: str):
    if cmd == "install":
        install()
        sys.exit(0)

    if cmd == "test":
        do_tests()
        sys.exit(0)

    # check node binary
    if which("stacks-node") is None:
        error_response(1)

    # check / create default config file
    if not os.path.isfile(get_config_path()):
        with open(get_config_path(), "w") as f:
            f.write(DEFAULT_CONFIG)
            f.close()

    if cmd == "status":
        status()

    if cmd == "start":
        start()

    if cmd == "stop":
        stop()

    if cmd == "config":
        config(arg)

    if cmd == "web":
        web()
