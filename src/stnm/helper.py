import os
from pathlib import Path


def config_path() -> str:
    return os.path.abspath(os.path.join(str(Path.home()), "stnm.conf"))
