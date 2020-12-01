import argparse
import re
from stnm.cli.common.response import error_response, success_response
import toml
from stnm.cli.common.util import config_path


class NotValidValue(Exception):
    pass


def bool_validator(s: str) -> bool:
    if s in ["true", "True"]:
        return True

    if s in ["false", "False"]:
        return False

    raise NotValidValue("Not a valid boolean value")


def str_validator(s: str) -> str:
    return s


def int_validator(s: str):
    if re.compile("^[0-9]+$").match(s):
        return int(s)

    raise NotValidValue("Not a valid integer value")


PARAMS = {
    "node.miner": bool_validator,
    "node.seed": str_validator,
    "burnchain.burn_fee_cap": int_validator,
    "burnchain.process_exit_at_block_height": int_validator,
    "burnchain.rpc_port": int_validator,
    "burnchain.peer_port": int_validator
}


def config(arg: str):
    param_value = arg.split("=")
    if len(param_value) != 2:
        return

    [param, raw_value] = param_value

    if param not in PARAMS:
        pass

    try:
        value = PARAMS[param](raw_value)
    except NotValidValue as ex:
        print(ex)
        return

    with open(config_path(), "r") as f:
        config_contents = f.read()
        f.close()

    [section, key] = param.split(".")

    parsed = toml.loads(config_contents)
    parsed[section][key] = value

    with open(config_path(), "w") as f:
        f.write(toml.dumps(parsed))
        f.close()

    success_response(4)
