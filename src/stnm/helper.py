import os
from pathlib import Path


def get_config_path() -> str:
    return os.path.abspath(os.path.join(str(Path.home()), "stnm.conf"))


