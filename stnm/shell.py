import os
import shutil
from typing import Optional

from stnm.constants import CARGO_BIN_PATH

env = os.environ.copy()
env["PATH"] = cargo_bin_path + os.path.pathsep + env["PATH"]


def which(name: str) -> Optional[str]:
    return shutil.which(name, path=env["PATH"])
