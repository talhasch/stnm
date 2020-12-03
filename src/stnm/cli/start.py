import os
import subprocess

from stnm.cli.common.process import get_node_process
from stnm.cli.common.response import error_response, success_response
from stnm.helper import config_path


def start():
    process = get_node_process()
    if process is not None:
        error_response(3)

    devnull = open(os.devnull, 'wb')
    process = subprocess.Popen(["stacks-node", "start", "--config", config_path()], stdout=devnull, stderr=devnull)
    success_response(3, **{"pid": process.pid})
