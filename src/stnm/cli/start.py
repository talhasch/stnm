import os
import subprocess

from stnm.cli.common.process import get_node_process
from stnm.cli.common.response import error_response, success_response
from stnm.helper.config import get_config_path, get_config_parsed, put_config_parsed


def start():
    process = get_node_process()
    if process is not None:
        error_response(3)

    config = get_config_parsed()
    if "__modified__" in config:
        del config["__modified__"]
        put_config_parsed(config)

    devnull = open(os.devnull, 'wb')
    process = subprocess.Popen(["stacks-node", "start", "--config", get_config_path()], stdout=devnull, stderr=devnull)
    success_response(3, **{"pid": process.pid})
