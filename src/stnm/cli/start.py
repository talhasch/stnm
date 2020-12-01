from stnm.cli.common.util import which
from stnm.cli.common.response import error_response
from stnm.cli.common.process import get_node_process
from stnm.cli.common.constants import DEFAULT_CONFIG

from pathlib import Path
import os

home_path = str(Path.home())


def start():
    process = get_node_process()
    if process is not None:
        error_response("stacks-node is already running")


    # check if its already working
    # check stacks-node binary
    # check conf file. create if not exist
