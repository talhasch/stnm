import re

import toml

from stnm.cli.common.response import error_response, success_response
from stnm.helper import get_config_path


class NotValidValue(Exception):
    pass


def bool_validator(s: str) -> bool:
    if s in ["true", "True"]:
        return True

    if s in ["false", "False"]:
        return False

    raise NotValidValue("{} is not a valid boolean value. Use True or true or False or false".format(s))


def str_validator(s: str) -> str:
    return s


def int_validator(s: str):
    if re.compile("^[0-9]+$").match(s):
        return int(s)

    raise NotValidValue("{} is not a valid integer value".format(s))


PARAMS = {
    "node.miner": bool_validator,
    "node.seed": str_validator,
    "burnchain.burn_fee_cap": int_validator,
    "burnchain.process_exit_at_block_height": int_validator,
    "burnchain.rpc_port": int_validator,
    "burnchain.peer_port": int_validator
}


def config(arg: str):
    with open(get_config_path(), "r") as f:
        config_contents = f.read()
        f.close()

    if arg == "show":
        print("-" * 60)
        print("Config file located at: {}".format(config_path()))
        print("-" * 60)
        print(config_contents)
        print("-" * 60)
        return

    param_value = arg.split("=")
    if len(param_value) != 2:
        error_response(5, arg)

    [param, raw_value] = param_value

    if param not in PARAMS:
        error_response(6, param)

    try:
        value = PARAMS[param](raw_value)
    except NotValidValue as ex:
        error_response(7, str(ex))
        return

    [section, key] = param.split(".")

    parsed = toml.loads(config_contents)
    parsed[section][key] = value

    with open(get_config_path(), "w") as f:
        f.write(toml.dumps(parsed))
        f.close()

    success_response(4)
