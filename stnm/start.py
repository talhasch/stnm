import subprocess

from stnm.config import get_config_path, get_config_parsed, put_config_parsed
from stnm.constants import DEV_NULL
from stnm.response import error_response, success_response
from stnm.shell import env
from stnm.shell import get_node_process


def start():
    process = get_node_process()
    if process is not None:
        error_response(3)

    config = get_config_parsed()
    if "__modified__" in config:
        del config["__modified__"]
        put_config_parsed(config)

    process = subprocess.Popen(["stacks-node", "start", "--config", get_config_path()], env=env, stdout=DEV_NULL, stderr=DEV_NULL)
    success_response(3, **{"pid": process.pid})
