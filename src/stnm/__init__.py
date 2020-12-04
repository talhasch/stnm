import os

from stnm.cli.common.constants import DEFAULT_CONFIG
from stnm.cli.common.response import error_response
from stnm.cli.common.util import which
from stnm.cli.config import config
from stnm.cli.install import install
from stnm.cli.start import start
from stnm.cli.status import status
from stnm.cli.stop import stop
from stnm.helper.config import get_config_path
from stnm.test import do_tests
from stnm.web import web


def main(cmd: str, arg: str):
    if cmd == "install":
        install()

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

    if cmd == "test":
        do_tests()
