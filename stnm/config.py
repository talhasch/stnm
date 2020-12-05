import os
import re
from typing import Dict
from typing import Union, List

import toml

from stnm.constants import HOME_PATH
from stnm.response import error_response, success_response


def get_config_path() -> str:
    return os.path.abspath(os.path.join(HOME_PATH, "stnm.conf"))


def get_config() -> str:
    with open(get_config_path(), "r") as f:
        config_contents = f.read()
        f.close()

    return config_contents


def get_config_parsed() -> Dict:
    with open(get_config_path(), "r") as f:
        config_contents = f.read()
        f.close()

    return toml.loads(config_contents)


def put_config_parsed(obj: Dict):
    with open(get_config_path(), "w") as f:
        f.write(toml.dumps(obj))
        f.close()


"""
Config Input Structure

        +---------------------+
        |      parameter      |
        +---------------------+
input = burnchain.burn_fee_cap=20000000
        |section |     key    | value |
        +-----------------------------+
        |        config entry         |
        +-----------------------------+
        
"""


class InvalidConfigEntry(Exception):
    pass


class UnavailableConfigParameter(Exception):
    pass


class InvalidValue(Exception):
    pass


def bool_validator(s: str) -> bool:
    if s in ["true", "True"]:
        return True

    if s in ["false", "False"]:
        return False

    raise InvalidValue("{} is not a valid boolean value. Use True or true or False or false".format(s))


def str_validator(s: str) -> str:
    return s


def int_validator(s: str):
    if re.compile("^[0-9]+$").match(s):
        return int(s)

    raise InvalidValue("{} is not a valid integer value".format(s))


AVAILABLE_PARAMS = {
    "node.miner": bool_validator,
    "node.seed": str_validator,
    "burnchain.burn_fee_cap": int_validator,
    "burnchain.process_exit_at_block_height": int_validator,
    "burnchain.rpc_port": int_validator,
    "burnchain.peer_port": int_validator
}


class ConfigEntry:
    def __init__(self, section: str, key: str, value: Union[str, int, bool]):
        self.section = section
        self.key = key
        self.value = value

    def __repr__(self):
        return "<{}.{}={}>".format(self.section, self.key, self.value)


def config_input_parser(input_: str) -> List[ConfigEntry]:
    rv = []
    entries = input_.split(",")

    for entry in entries:
        param_split = entry.split("=")
        if len(param_split) != 2:
            raise InvalidConfigEntry(entry)

        [param, raw_value] = param_split
        if param not in AVAILABLE_PARAMS:
            raise UnavailableConfigParameter(param)

        value = AVAILABLE_PARAMS[param](raw_value)

        [section, key] = param.split(".")

        rv.append(ConfigEntry(section, key, value))

    return rv


def config(input_: str):
    if input_ == "show":
        config_contents = get_config()
        print("-" * 60)
        print("Config file located at: {}".format(get_config_path()))
        print("-" * 60)
        print(config_contents)
        print("-" * 60)
        return

    try:
        entries = config_input_parser(input_)
    except InvalidConfigEntry as ex:
        error_response(5, str(ex))
        return
    except UnavailableConfigParameter as ex:
        error_response(6, str(ex))
        return
    except InvalidValue as ex:
        error_response(7, str(ex))
        return

    parsed = get_config_parsed()

    for e in entries:
        parsed[e.section][e.key] = e.value

    parsed["__modified__"] = True

    put_config_parsed(parsed)

    success_response(4)
