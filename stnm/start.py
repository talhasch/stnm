import subprocess

from stnm.config import get_config_path, get_config_parsed, put_config_parsed
from stnm.path import devnull
from stnm.process import get_node_process
from stnm.response import error_response, success_response
from stnm.shell import env


def start():
    process = get_node_process()
    if process is not None:
        error_response(3)

    config = get_config_parsed()
    if "__modified__" in config:
        del config["__modified__"]
        put_config_parsed(config)

    process = subprocess.Popen(["stacks-node", "start", "--config", get_config_path()], env=env, stdout=devnull, stderr=devnull)
    success_response(3, **{"pid": process.pid})
