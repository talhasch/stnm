import os
from pathlib import Path
from typing import Dict

import toml


def get_config_path() -> str:
    return os.path.abspath(os.path.join(str(Path.home()), "stnm.conf"))


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
